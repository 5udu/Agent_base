# FastAPI + LangChain 教学项目

这是一个面向初学者的工程化 AI 示例项目。

它使用：

- `FastAPI` 提供接口
- `LangChain` 组织模型调用
- 火山方舟 OpenAI 兼容接口接入豆包模型

这个项目的重点不是功能复杂，而是让你快速看懂一个最小但分层清晰的 AI 工程。

## 快速开始

环境要求：`Python 3.10+`

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 复制环境变量模板

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

3. 打开 `.env`，填写你自己的密钥

```env
ARK_API_KEY=your_api_key_here
```

4. 启动项目

```bash
uvicorn main:app --reload
```

启动后可访问：

- 文档：`http://127.0.0.1:8000/docs`
- 健康检查：`http://127.0.0.1:8000/health`

## 项目结构

```text
project/
├── main.py
├── .env.example
├── requirements.txt
├── README.md
└── app/
    ├── api/
    │   ├── chat.py
    │   └── health.py
    ├── schemas/
    │   └── chat.py
    ├── services/
    │   └── chat_service.py
    ├── core/
    │   ├── config.py
    │   └── logger.py
    ├── agents/
    │   └── chat_agent.py
    └── models/
        └── llm_client.py
```

## 分层说明

- `main.py`：应用入口，注册路由
- `app/api`：接口层，处理 HTTP 请求
- `app/schemas`：数据模型层，定义请求和响应结构
- `app/services`：业务层，连接接口和智能体
- `app/agents`：智能体层，组织提示词和消息
- `app/models`：模型层，封装 LangChain 模型客户端
- `app/core`：基础设施层，管理配置和日志

## 调用链路

```text
Request -> API -> Service -> Agent -> LLM Client -> Model -> Response
```

## 默认模型配置

```env
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
ARK_MODEL=doubao-seed-2-0-pro-260215
```

项目不会内置真实 `ARK_API_KEY`。
如果未配置密钥，调用对话接口时会提示先填写 `.env`。

## 接口示例

`POST /chat`

```json
{
  "message": "请解释什么是 LangChain？"
}
```

返回示例：

```json
{
  "reply": "LangChain 是一个帮助你组织大模型调用流程的开发框架。"
}
```

## 适合怎么学

推荐按下面顺序阅读：

1. `main.py`
2. `app/api/chat.py`
3. `app/services/chat_service.py`
4. `app/agents/chat_agent.py`
5. `app/models/llm_client.py`
6. `app/core/config.py`

这样可以顺着一次请求的完整链路，快速理解这个教学项目的工程结构。
