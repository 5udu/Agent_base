"""应用入口模块。

该模块负责创建 FastAPI 应用实例并注册路由，是整个教学项目的启动入口。
设计上保持尽量轻量，避免把业务逻辑放在入口文件中，便于初学者理解工程分层。
"""

from fastapi import FastAPI

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
