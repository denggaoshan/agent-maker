"""Plugin class"""
# pylint: disable=unused-argument
from typing import List

from common import Message


class Plugin:
    """Plugin class"""
    name = ''

    def __init__(self) -> None:
        pass

    def build_system_prompt(self, messages: List[Message]) -> List[Message]:
        """Build system prompt"""
        return ''

    def build_template_prompt(self, messages: List[Message]) -> List[Message]:
        """Build template prompt"""
        return ''

    @classmethod
    def build_from_toml(cls, toml: dict):
        """Build from toml file"""
        raise NotImplementedError
