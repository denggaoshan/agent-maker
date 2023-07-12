"""Common classes"""
from typing import List, Optional, Tuple

class Message:
    """Chat message"""
    def __init__(self,
                 speaker: Optional[str] = None,
                 content: Optional[str] = None,
                 is_user: bool = False
                 ) -> None:
        self.speaker: str = speaker
        self.content: str = content
        self.is_user = is_user

    def __str__(self) -> str:
        if self.speaker is None:
            return str(self.content)
        return f'{self.speaker}: {self.content}'

    @staticmethod
    def to_str(messages: list) -> str:
        """Convert a list of messages to a string"""
        return '\n'.join([str(message) for message in messages])

    @staticmethod
    def from_str(message: str, is_user: bool = False) -> 'Message':
        """Convert a string to a message"""
        if ': ' in message:
            speaker, content = message.split(': ', maxsplit=1)
            return Message(speaker=speaker, content=content, is_user=is_user)
        return Message(content=message, is_user=is_user)

    def get_chat_message(self) -> Tuple[str, str]:
        """Get chat message"""
        if self.is_user:
            return 'user', self.content
        return 'assistant', self.content

    @staticmethod
    def from_list(messages: List[str]) -> List['Message']:
        """Convert a list of messages to a string"""
        return [Message.from_str(message) for message in messages]

    @staticmethod
    def from_dict(message: dict) -> 'Message':
        """Convert a dict to a message"""
        assert 'role' in message
        assert 'content' in message
        return Message(speaker=message['speaker'], content=message['content'])
