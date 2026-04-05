"""模型客户端模块。

该模块负责封装 LangChain 模型初始化逻辑，向上层隐藏具体模型供应商接入细节。
设计上保持单一职责，便于后续替换模型平台时只改这一处。
"""

from langchain_openai import ChatOpenAI

from app.core.config import PLACEHOLDER_API_KEY, settings


def get_chat_model() -> ChatOpenAI:
    """创建 LangChain 对话模型客户端。

    Args:
        无。

    Returns:
        ChatOpenAI: 对话模型实例。

    Raises:
        ValueError: 当 `ARK_API_KEY` 为空或仍为占位值时抛出。
    """
    # NOTE: 公开仓库不内置真实密钥，因此在模型初始化前做一次明确校验。
    if settings.ark_api_key in {"", PLACEHOLDER_API_KEY}:
        raise ValueError(
            "ARK_API_KEY is not set. Copy .env.example to .env and fill in your API key."
        )

    return ChatOpenAI(
        model=settings.ark_model,
        api_key=settings.ark_api_key,
        base_url=settings.ark_base_url,
        temperature=0.2,
    )
