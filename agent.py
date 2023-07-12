"""Agent class"""
import importlib
import inspect
import os
from typing import List, Tuple

from fastapi import Request
from langchain import PromptTemplate
from langchain.llms import AzureOpenAI, BaseLLM, OpenAI
import toml

from common import Message
from plugins.base import Plugin

TEMPLATE = """{system}
{template}
Begin!
{chat_history}
{role_assistant}:"""


class Agent:
    """Agent class"""
    def __init__(self,
                 config_path: str = None,
                 name: str = None,
                 router: str = None,
                 role_assistant: str = None,
                 role_user: str = None,
                 greeting: str = None,
                 llm: BaseLLM = None,
                 plugins: list = None):
        self.name = name or 'Agent'
        self.config_path = config_path or None
        self.router = router
        self.role_assistant = role_assistant or 'assistant'
        self.role_user = role_user or 'user'
        self.greeting = greeting or f'Hello, I am {self.name}.'

        self.prompt = PromptTemplate.from_template(TEMPLATE)

        self._llm: BaseLLM = llm
        self._plugins = plugins or []


    def _build_chat_history(self, messages: List[Message]) -> str:
        """Build chat history"""
        return Message.to_str(messages)


    def _build_prompt(self, messages: List[Message]) -> str:
        """Build prompt"""
        system, template = '', ''
        for plugin in self._plugins:
            temp_system = Message.to_str(plugin.build_system_prompt(messages))
            system += '\n' + temp_system if temp_system else ''
            temp_template = Message.to_str(plugin.build_template_prompt(messages))
            template += '\n' + temp_template if temp_template else ''

        return self.prompt.format(
            system=system,
            template=template,
            chat_history=Message.to_str(messages),
            role_assistant=self.role_assistant,
        )

    @classmethod
    def _load_llm(cls, data: dict):
        """Load LLM model"""
        if 'name' not in data:
            raise ValueError('LLM name not found')
        if data['name'] == 'openai':
            return OpenAI(openai_api_key=data['api_key'])
        if data['name'] == 'azure':
            return AzureOpenAI(
                openai_api_type='azure',
                openai_api_version=data['api_version'],
                openai_api_key=data['api_key'],
                openai_api_base=data['api_base'],
                deployment_name=data['deployment_name']
            )
        raise ValueError(f'LLM {data["name"]} not found')

    @classmethod
    def _load_plugins(cls, data: dict) -> List[Plugin]:
        plugin_classes = {}
        for path in os.listdir('plugins'):
            if not path.endswith('.py') or path == '__init__.py' or path == 'base.py':
                continue
            plugin_module = importlib.import_module('plugins.' + path[:-3])
            # Find all plugin classes
            for _, obj in inspect.getmembers(plugin_module, inspect.isclass):
                if not issubclass(obj, Plugin) or obj == Plugin:
                    continue
                plugin_classes[obj.name] = obj
        plugins = []
        for plugin_data in data:
            plugin_name = plugin_data['name']
            try:
                plugin_class = plugin_classes[plugin_name]
            except KeyError as ex:
                raise ValueError(f'Plugin {plugin_name} not found') from ex
            plugin = plugin_class.build_from_toml(plugin_data)
            plugins.append(plugin)
        return plugins

    def chat(self, messages: List[Message]) -> Tuple[str, str]:
        """Chat with the agent"""
        prompt = self._build_prompt(messages)
        response = self._llm(prompt, stop='\n')
        return prompt, response

    async def handle(self, request: Request):
        """Handle the request"""
        data = await request.json()
        messages = data.get('messages', [])
        if isinstance(messages, list):
            messages = Message.from_list(messages)
        else:
            messages = [Message.from_str(messages)]
        _, result = self.chat(messages)
        return {"result": result}

    @classmethod
    def build_from_toml(cls, filename: str):
        """Build Agent from TOML file"""
        toml_data = toml.load(filename)

        return cls(
            config_path=filename,
            name=toml_data['profile'].get('name'),
            role_assistant=toml_data['profile'].get('role_assistant'),
            role_user=toml_data['profile'].get('role_user'),
            greeting=toml_data['profile'].get('greeting'),
            router=toml_data['profile'].get('router'),
            llm=cls._load_llm(toml_data['llm']),
            plugins=cls._load_plugins(toml_data['plugins'])
        )
