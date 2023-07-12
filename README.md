[English](README_en.md) | [中文](README.md)

# Agent Maker
本项目旨在
1. 通过toml格式快速定义对话机器人，无须动手写代码。
2. 提供丰富的插件组件，可以像搭积木一样组装成对话机器人。
3. 提供调试工作台，可以在线debug

# 说明

我们目前不提供大模型服务，目前支持openai（需要科学上网）和azure接口，自己去弄api_key，或者自己搭建大模型服务然后接入进来。

# 安装要求
```
pip install -r requirements.txt
```

# 开始制作第一个Agent

[示例1](./agents/cn_robot.toml)

```
[profile]
name = '老李'
router = '/li'

[llm]
name = 'openai'
api_key = '<your-openai-api-key>'  # 需要替换成你的api-key
```

您可以创建任意数量的机器人，只需将它们全部放在 agents 目录中，会自动生效，请使用不同的路由地址。

# 如何用api模式运行

您可以运行以下命令来启动服务器：
```
uvicorn main:app --reload --port 5000
```


```
curl --location 'http://127.0.0.1:5000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "messages": [
        "user: Hello"
    ]
}'

Response:
{"result":" Hi there! How may I help you?"}
```
![图片](./docs/imgs/api_demo.jpg)

# 如何用web模式运行

```
streamlit run web.py
```

![demo](./docs/imgs/waiter_demo_cn.jpg)

# 接入LLM

所有的Agent都需要底层的LLM模型驱动，目前支持openai接口，以及azure的接口

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

