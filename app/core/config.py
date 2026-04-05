"""应用配置模块。

该模块负责集中读取环境变量并生成只读配置对象。
设计意图是把所有运行期配置收拢到一个地方，便于教学时理解“配置优先于硬编码”的工程实践。
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


# NOTE: 火山方舟 OpenAI 兼容接口地址，教学项目默认指向北京区公共入口。
DEFAULT_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
# NOTE: 教学项目默认使用的豆包模型名称，适合作为最小示例配置。
DEFAULT_MODEL = "doubao-seed-2-0-pro-260215"
# NOTE: 环境变量模板中的占位值，用于识别“用户尚未填写真实密钥”的状态。
PLACEHOLDER_API_KEY = "your_api_key_here"


@dataclass(frozen=True)
class Settings:
    """应用运行配置对象。

    功能简述：保存应用运行所需的核心配置。
    设计意图：统一配置入口，避免分散读取环境变量。
    核心属性：包含应用名、版本、调试开关和模型接入参数。
    使用场景：供各模块共享读取。
    注意事项：`ark_api_key` 允许为空，便于公开仓库本地配置。
    """

    app_name: str
    app_version: str
    debug: bool
    ark_base_url: str
    ark_model: str
    ark_api_key: str


# NOTE: 统一在模块加载时读取 `.env`，让其余模块直接消费 `settings` 即可。
load_dotenv()

# NOTE: 全局配置对象只创建一次，便于在整个应用中复用。
settings = Settings(
    app_name=os.getenv("APP_NAME", "LangChain Teaching API"),
    app_version=os.getenv("APP_VERSION", "0.1.0"),
    debug=os.getenv("DEBUG", "true").lower() == "true",
    ark_base_url=os.getenv("ARK_BASE_URL", DEFAULT_BASE_URL),
    ark_model=os.getenv("ARK_MODEL", DEFAULT_MODEL),
    ark_api_key=os.getenv("ARK_API_KEY", ""),
)
