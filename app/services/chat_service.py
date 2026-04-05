"""对话业务服务模块。

该模块位于接口层和智能体层之间，负责承接业务语义并转发给智能体。
设计上故意保持简单，用来强调服务层在工程分层中的职责边界。
"""

from app.agents.chat_agent import ChatAgent, get_chat_agent


class ChatService:
    """对话业务服务。

    功能简述：接收用户消息并调用智能体生成回复。
    设计意图：隔离接口层和模型编排层。
    核心属性：chat_agent (ChatAgent) 表示对话智能体。
    使用场景：由接口层调用。
    注意事项：当前服务层保持最小实现。
    """

    def __init__(self, chat_agent: ChatAgent) -> None:
        """初始化对话业务服务。

        Args:
            chat_agent (ChatAgent): 对话智能体实例。

        Returns:
            None: 仅完成初始化。

        Raises:
            无。
        """
        self.chat_agent = chat_agent

    def chat(self, message: str) -> str:
        """根据用户消息生成回复。

        Args:
            message (str): 用户输入的消息文本。

        Returns:
            str: 智能体生成的回复文本。

        Raises:
            ValueError: 当模型客户端缺少有效密钥时抛出。
        """
        return self.chat_agent.reply(message)


def get_chat_service() -> ChatService:
    """创建默认对话业务服务。

    Args:
        无。

    Returns:
        ChatService: 默认服务实例。

    Raises:
        ValueError: 当依赖链上的模型客户端缺少有效密钥时抛出。
    """
    return ChatService(chat_agent=get_chat_agent())
