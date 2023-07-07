# Agent Maker
您可以通过编写一些 toml 格式的配置文件来快速创建机器人。

# 安装要求
```
pip install -r requirements.txt
```

# 制作您自己的机器人

您可以查看 agents/robot.toml:

```
[profile]
name = 'Tom'
router = '/chat'  # 您的机器人的路由

[llm]
name = 'openai'
api_key = '<your-openai-api-key>'  # 您的 OPENAI_API_KEY

[[plugins]]  # 可选的
name = 'system'
prompt = "You are a robot. You must answer questions."

[[plugins]]  # 可选的
name = 'domain-expert'
domain = 'law'
occupation = 'lawyer'

```

您可以创建任意数量的机器人，只需将它们全部放在 agents 目录中，并请使用不同的路由。

# 如何运行

您可以运行以下命令来启动服务器：
```
uvicorn main:app --reload --port 5000
```

然后：

```
curl --location 'http://127.0.0.1:5000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "messages": [
        "user: Hello"
    ]
}'
```

您将获得以下响应：
```
{"result":" Hi there! How may I help you?"}
```

# 插件

您可以使用插件系统来自定义您的机器人。目前，我们提供一些基本的插件功能，并将在未来提供更多插件支持。