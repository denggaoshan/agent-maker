"""Common classes"""
from typing import List, Optional


class Message:
    """Chat message"""
    def __init__(self,
                 speaker: Optional[str] = None,
                 content: Optional[str] = None) -> None:
        self.speaker: str = speaker
        self.content: str = content

    def __str__(self) -> str:
        if self.speaker is None:
            return str(self.content)
        return f'{self.speaker}: {self.content}'

    @staticmethod
    def to_str(messages: list) -> str:
        """Convert a list of messages to a string"""
        return '\n'.join([str(message) for message in messages])

    @staticmethod
    def from_str(message: str) -> 'Message':
        """Convert a string to a message"""
        if ': ' in message:
            speaker, content = message.split(': ', maxsplit=1)
            return Message(speaker=speaker, content=content)
        return Message(content=message)

    @staticmethod
    def from_list(messages: List[str]) -> List['Message']:
        """Convert a list of messages to a string"""
        return [Message.from_str(message) for message in messages]
