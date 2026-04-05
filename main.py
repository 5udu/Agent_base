"""应用入口模块。

该模块负责创建 FastAPI 应用实例并注册路由，是整个教学项目的启动入口。
设计上保持尽量轻量，避免把业务逻辑放在入口文件中，便于初学者理解工程分层。
"""

from fastapi import FastAPI
import uvicorn

from app.api.chat import chat_router
from app.api.health import health_router
from app.core.config import settings
from app.core.logger import logger

# NOTE: 启动日志放在模块加载阶段，便于本地调试时快速确认配置是否生效。
logger.info("App started: %s, debug=%s", settings.app_name, settings.debug)

# NOTE: 全局应用实例由 Uvicorn 直接导入，名称保持为 app 便于社区工具识别。
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    description="A teaching project for FastAPI + LangChain layering.",
)
app.include_router(chat_router)
app.include_router(health_router)


def run() -> None:
    """启动 FastAPI 应用。

    Args:
        无。

    Returns:
        None: 仅负责启动本地开发服务。

    Raises:
        无。
    """
    # NOTE: 保留独立启动函数，便于 `python main.py` 和其他脚本复用。
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    run()
