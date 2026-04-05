"""对话智能体模块。

该模块负责组织系统提示词和用户消息，并调用 LangChain 模型对象完成回复生成。
设计意图是将“提示词编排”与“业务调用入口”解耦，便于后续扩展多轮对话或工具调用。
"""

from langchain_core.messages import HumanMessage, SystemMessage

from app.models.llm_client import get_chat_model


class ChatAgent:
    """对话智能体。

    功能简述：组织提示词并调用模型生成回复。
    设计意图：集中管理消息编排逻辑。
    核心属性：llm 表示已初始化的对话模型实例。
    使用场景：由业务服务层调用。
    注意事项：当前使用固定系统提示词。
    """

    def __init__(self) -> None:
        """初始化对话智能体。

        Args:
            无。

        Returns:
            None: 仅完成初始化。

        Raises:
            ValueError: 当模型客户端缺少有效密钥时抛出。
        """
        self.llm = get_chat_model()

    def reply(self, message: str) -> str:
        """根据用户输入生成教学风格回复。

        Args:
            message (str): 用户输入的消息内容。

        Returns:
            str: 大模型生成的回复文本。

        Raises:
            ValueError: 当模型客户端缺少有效密钥时抛出。
        """
        # NOTE: 系统提示词固定为“耐心教学助手”，方便课堂演示时稳定输出风格。
        # TODO: 后续可在这里注入历史消息，扩展为多轮对话教学示例。
        messages = [
            SystemMessage(
                content=(
                    "You are a patient teaching assistant. "
                    "Explain clearly, give practical examples, and keep answers easy to follow."
                )
            ),
            HumanMessage(content=message),
        ]
        response = self.llm.invoke(messages)
        return response.content


def get_chat_agent() -> ChatAgent:
    """创建默认对话智能体。

    Args:
        无。

    Returns:
        ChatAgent: 默认智能体实例。

    Raises:
        ValueError: 当模型客户端缺少有效密钥时抛出。
    """
    return ChatAgent()
