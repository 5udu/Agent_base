"""对话接口模块。

该模块负责暴露 `/chat` HTTP 接口，把外部请求转交给业务层处理。
设计意图是让接口层只处理协议相关工作，不直接接触模型调用细节。
"""

from fastapi import APIRouter, Depends

from app.core.logger import logger
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService, get_chat_service

# NOTE: 对话路由统一挂载在 `/chat`，便于后续继续扩展多轮对话接口。
chat_router = APIRouter(prefix="/chat", tags=["chat"])


@chat_router.post("", response_model=ChatResponse)
def chat(
    req: ChatRequest,
    service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    """处理用户对话请求并返回模型回复。

    Args:
        req (ChatRequest): 用户提交的请求体。
        service (ChatService): 对话业务服务实例。

    Returns:
        ChatResponse: 包含模型回复的响应对象。

    Raises:
        ValueError: 当模型客户端未配置有效密钥时抛出。
    """
    logger.info("收到聊天请求: %s", req.message)
    reply = service.chat(req.message)
    return ChatResponse(reply=reply)
