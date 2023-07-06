"""System plugin for adding system prompt"""
from typing import List

from overrides import override

from common import Message
from plugins.base import Plugin


class SystemPlugin(Plugin):
    """System plugin for adding system prompt"""
    name = 'system'
    def __init__(self, prompt) -> None:
        super().__init__()
        self._prompt = prompt

    @classmethod
    @override
    def build_from_toml(cls, toml: dict):
        """Build from toml file"""
        assert toml['name'] == cls.name
        return cls(toml['prompt'])

    @override
    def build_system_prompt(self, messages: List[Message]) -> List[Message]:
        return [
            Message(content=self._prompt)
        ]
