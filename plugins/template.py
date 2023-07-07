"""Template plugin for adding template prompt. The template prompt is a prompt that is added after the system prompt.
Usually, the template prompt is used to give a standard format to the system prompt.
Uasge:
[[plugins]]
name = 'template'
prompt = (str)
"""
from typing import List

from overrides import override

from common import Message
from plugins.base import Plugin


class TemplatePlugin(Plugin):
    """Template plugin for adding system prompt"""
    name = 'template'
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
    def build_template_prompt(self, messages: List[Message]) -> List[Message]:
        """Build template prompt"""
        return [Message(content=self._prompt)]
