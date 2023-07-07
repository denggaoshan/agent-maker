"""Domain expert plugin for adding domain expert prompt. Use this plugin to give a identity to the assistant.
Usage:
[[plugins]]
name = 'domain-expert'
domain = 'law'
occupation = 'lawyer'
"""
from typing import List

from overrides import override

from common import Message
from plugins.base import Plugin


class DomainExpertPlugin(Plugin):
    """Domain expert plugin for adding domain expert prompt"""
    name = 'domain-expert'
    def __init__(self, domain, occupation) -> None:
        super().__init__()
        self._domain = domain
        self._occupation = occupation

    @classmethod
    @override
    def build_from_toml(cls, toml: dict):
        """Build from toml file"""
        assert toml['name'] == cls.name
        return cls(toml['domain'], toml['occupation'])

    @override
    def build_system_prompt(self, messages: List[Message]) -> List[Message]:
        """Build system prompt"""
        return [
            Message(content=f'You are a {self._occupation} in {self._domain}'),
            Message(content='Please use the domain knowledge to help the user as much as possible.')
        ]

    @override
    def build_template_prompt(self, messages: List[Message]) -> List[Message]:
        """Build template prompt"""
        return [
            Message('user', 'Hi, who are you?'),
            Message('assistant', f'I am a {self._occupation} in {self._domain}. What can I help you?'),
        ]
