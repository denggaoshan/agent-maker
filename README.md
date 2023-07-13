[English](README_en.md) | [中文](README.md)

# Agent Maker
本项目旨在
1. 通过toml格式快速创建定制个性化的Agent，无须动手写代码。
2. 提供丰富的插件组件，可以像搭积木一样组装成对话机器人。
3. 提供工作台，可以在线调试prompt来debug对应的agent

# 说明

我们目前不提供大模型服务，目前支持openai（需要科学上网）和azure接口，自己去弄api_key。
或者自己搭建大模型服务然后接入（TODO）

# 安装要求
```
pip install -r requirements.txt
```

# 开始制作第一个Agent

[示例1](./agents/demo_cn/robot.toml)

```
[profile]
name = '老李'
router = '/li'

[llm]
name = 'openai'
api_key = '<your-openai-api-key>'  # 需要替换成你的api-key
```

可以创建任意数量的机器人，只需将它们全部放在 agents 目录中，会自动生效，请使用不同的路由地址。

# 如何用api模式运行

您可以运行以下命令来启动API服务：
```
uvicorn main:app --reload --port 5000
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

可以填写API KEY，也可以提前导入环境变量：
```
export OPENAI_API_KEY='<your-openai-api-key>'
```

[配置示例](./agents/demo_cn/robot.toml)

```
[profile]
name = '老李'
router = '/li'

[llm]
name = 'openai'
api_key = '<your-openai-api-key>'
```

## Azure接口

[配置示例](./agents/demo_cn/robot_azure.toml)


```
[profile]
name = '老李'
router = '/li2'
greeting = '你好，我是老李，你想和我聊点什么？'
role_assistant = '老李'
role_user = '用户'

[llm]
name = 'azure'
api_version = '2023-03-15-preview'
deployment_name = 'gpt-35-turbo'
api_base = '<your api base>'
api_key = '<your api key>'

[[plugins]]
name = 'character-common'
```

# 插件系统 (Plugin)

通过在toml文件中组装各种插件，可以快速定制出一个Agent

## System插件

系统插件通常放在prompt开头，用来：

1.Agent身份

2.Agent的行为规则


## Character Commmon 插件

强化Agent对于自己的身份认知，避免Agent被套话，比如你是Gpt这种问题，举例：

[配置示例](./agents/demo_cn/robot_azure.toml)

![回答](./docs/imgs/cn_charactor.jpg)

![回答](./docs/imgs/cn_charactor_gpt.jpg)


## Retriever插件

Retriever插件将通过一些数据源生成prompt，例如：

1.Txt文件

2.数据库

目前，我们提供了一些基本的检索器插件，未来还会提供更多的检索器。


# TODO List

- [ ] LLM支持chatglm
- [ ] 支持连接向量数据库相关插件 
- [ ] 工作台可编辑配置功能
- [ ] 建设项目的文档

