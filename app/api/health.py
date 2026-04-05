"""健康检查接口模块。

该模块提供最简单的运行状态探针，便于本地开发和部署平台检查服务是否启动成功。
同时返回当前应用名和模型名，方便教学时确认配置加载结果。
"""

from fastapi import APIRouter

from app.core.config import settings

# NOTE: 健康检查保持只读和轻量，避免依赖外部模型接口导致探针不稳定。
health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get("")
def health() -> dict[str, str]:
    """返回应用当前基础运行状态。

    Args:
        无。

    Returns:
        dict[str, str]: 包含服务状态和基础配置信息的字典。

    Raises:
        无。
    """
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "model": settings.ark_model,
    }
