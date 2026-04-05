"""日志模块。

该模块负责定义项目统一使用的日志对象。
教学场景下保留最基础的控制台日志格式，方便观察请求链路和配置加载结果。
"""

import logging

# NOTE: 教学项目采用统一日志格式，优先保证本地调试时可读性。
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# NOTE: 全局日志实例统一命名为 app，避免各模块分散创建导致输出风格不一致。
logger = logging.getLogger("app")
