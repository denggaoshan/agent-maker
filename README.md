[English](README_en.md) | [中文](README.md)

# Agent Maker
您可以通过编写一些 toml 格式的配置文件来快速创建机器人。

# 安装要求
```
pip install -r requirements.txt
```

如果你使用openai接口，则需要一个openai的api key， 需要写到agent的配置文件中

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

# 如何用api模式运行

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

![图片](./docs/imgs/api_demo.jpg)

# 如何用web模式运行

```
streamlit run web.py
```

# 效果演示

![demo](./docs/imgs/waiter_demo_cn.jpg)

# LLM系统

目前支持openai接口，以及azure的接口

## OpenAI接口

[配置示例](./agents/cn_robot.toml)

## Azure接口

[配置示例](./agents/cn_robot_azure.toml)

# 插件系统

您可以使用插件系统来自定义您的机器人。目前，我们提供一些基本的插件功能，并将在未来提供更多插件支持。



## System插件


系统插件可用于自定义机器人的系统设置，如：

1.机器人的身份

2.机器人的规则


## Template插件



模板插件可以用于自定义机器人的对话模板，它将引导机器人根据模板生成响应。


## Character Commmon 插件

强化Agent对于自己的身份认知，避免Agent被套话，比如你是Gpt这种问题，举例：

[配置示例](./agents/cn_robot_azure.toml)

![回答](./docs/imgs/cn_charactor.jpg)

![回答](./docs/imgs/cn_charactor_gpt.jpg)



## Retriever插件


Retriever插件将通过一些数据源生成prompt，例如：

1.Txt文件

2.数据库



目前，我们提供了一些基本的检索器插件，未来还会提供更多的检索器。

