from pydantic import BaseModel
from typing import Optional, List 

class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str

class MonitorPayload(BaseModel):
    channel_id: str
    return_url: str
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
