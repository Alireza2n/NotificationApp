from enum import Enum
from typing import TypedDict

from pydantic import BaseModel


class MessageDetails(TypedDict):
    body: str


class MessageMedium(str, Enum):
    telegram = 'telegram'


class Message(BaseModel):
    mediums: list[MessageMedium] = []
    recipients: list[str] = []
    message_detail: MessageDetails
