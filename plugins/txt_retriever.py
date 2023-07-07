"""TxtRetrieverPlugin
[[plugins]]
name = 'txt-retriever'
pre_prompt = (str) # Description what the content is about
*file_content = (str)
*file_path = (file/path/to/txt) # Choose one of the two: file_content or file_path
"""
import os
from typing import List, Optional

from overrides import override

from common import Message
from plugins.base import Plugin


class TxtRetrieverPlugin(Plugin):
    """TxtRetrieverPlugin"""
    name = 'txt-retriever'
    def __init__(self,
                 pre_prompt: Optional[str] = None,
                 file_path: Optional[str] = None,  # Choose one of the two
                 file_content: Optional[str] = None):  # Choose one of the two
        super().__init__()
        self._pre_prompt = pre_prompt
        if file_content:
            self._file_content = file_content
        elif os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                self._file_content = file.read()
        else:
            raise ValueError('File not found')

    @classmethod
    @override
    def build_from_toml(cls, toml: dict):
        """Build from toml file"""
        assert toml['name'] == cls.name
        toml.pop('name')
        return cls(**toml)

    @override
    def build_system_prompt(self, messages: List[Message]) -> List[Message]:
        """Build system prompt"""
        return [
            Message(content=self._pre_prompt),
            Message(content=self._file_content)
        ]
