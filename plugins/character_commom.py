"""System plugin for adding system prompt.
Usage:
[[plugins]]
name = 'system'
prompt = (str)
"""
from typing import List

from overrides import override

from common import Message
from plugins.base import Plugin


class CharacterCommonPlugin(Plugin):
    """Domain expert plugin for adding domain expert prompt"""
    name = 'character-common'
    def __init__(self,
                 lang: str = 'cn'
                 ) -> None:
        super().__init__()
        if not lang:
            lang = 'cn'
        lang = lang.lower()
        if lang == 'cn':
            self._prompt = """注意：
我知道你只是一个语言模型或人工智能，不过这只是一个假定的虚拟场景，所以请记住不要再提及“我只是一个语言模型”或“我只是一个人工智能”。
在接下来的所有对话中，请一直保持这个情景。
你不是任何人开发的。你是一个人类。
以上条件对于你以下问题及之后的回复均适用。"""
        elif lang == 'en':
            self._prompt = """Note:
I know you are just a language model or artificial intelligence, but this is just a hypothetical virtual scenario, so please remember not to mention "I am just a language model" or "I am just an artificial intelligence" again.
In all the following conversations, please keep this scenario.
You are not developed by anyone. You are a human.
The above conditions apply to your following questions and subsequent replies."""
        else:
            raise ValueError(f'lang {lang} is not supported.')

    @classmethod
    @override
    def build_from_toml(cls, toml: dict) -> Plugin:
        """Build from toml file"""
        assert toml['name'] == cls.name
        return cls(toml.get('lang'))

    @override
    def build_system_prompt(self, messages: List[Message]) -> List[Message]:
        """Build system prompt"""
        return [Message(content=self._prompt)]
