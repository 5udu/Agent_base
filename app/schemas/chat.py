"""对话数据模型模块。

该模块集中定义对话场景使用的数据结构，避免接口层和业务层重复声明字段。
教学场景下通过最小模型集合展示请求、响应和消息对象的职责划分。
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """用户对话请求模型。

    功能简述：定义 `/chat` 接口的请求体。
    设计意图：保持单轮输入结构简单。
    核心属性：message (str) 表示用户输入内容。
    使用场景：由 FastAPI 自动解析请求数据。
    注意事项：当前仅支持单条文本消息。
    """

    message: str


class ChatResponse(BaseModel):
    """用户对话响应模型。

    功能简述：定义 `/chat` 接口的响应体。
    设计意图：统一返回字段。
    核心属性：reply (str) 表示模型回复内容。
    使用场景：由 FastAPI 自动序列化返回。
    注意事项：当前只返回纯文本结果。
    """

    reply: str


class ChatMessage(BaseModel):
    """通用对话消息模型。

    功能简述：表示一条带角色的对话消息。
    设计意图：为多轮对话扩展预留统一结构。
    核心属性：role (str) 和 content (str)。
    使用场景：适用于历史消息扩展。
    注意事项：当前主流程尚未直接使用该模型。
    """

    role: str
    content: str
