from typing import List, Optional

from pydantic import BaseModel


class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str


class MonitorPayload(BaseModel):
    channel_id: Optional[str] = None
    return_url: Optional[str] = None
    settings: List[Setting]


class Event(BaseModel):
    title: str
    url: str
    start_time: Optional[str] = None
    venue: str


class EventRequest(BaseModel):
    city: Optional[str] = None
    dma_id: Optional[str] = None
    category: Optional[str] = None
    limit: int = 5
