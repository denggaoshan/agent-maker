"""Common classes"""
from typing import Optional


class Message:
    """Chat message"""
    def __init__(self,
                 speaker: Optional[str] = None,
                 content: Optional[str] = None) -> None:
        self.speaker: str = speaker
        self.content: str = content

    def __str__(self) -> str:
        if self.speaker is None:
            return self.content
        return f'{self.speaker}: {self.content}'

    @staticmethod
    def to_str(messages: list) -> str:
        """Convert a list of messages to a string"""
        return '\n'.join([str(message) for message in messages])
