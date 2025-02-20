from fastapi import APIRouter,  Query
from fastapi.responses import JSONResponse
import httpx
from app.services.events import EventService
from app.models.events import EventRequest,MonitorPayload
import logging
from app.config import Config


logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/events")
async def get_events(
    city: str = Query(None, description="City name"),
    dma_id: str = Query(None, description="DMA ID"),
    category: str = Query(None, description="Event category"),
    limit: int = Query(5, description="Number of events to fetch")
):
    return await EventService.get_formatted_events(city, dma_id, category, limit)


@router.post("/tick")
async def post_tick(payload: MonitorPayload):
    city = [s.default for s in payload.settings if s.label.startswith("city")]
    category = [s.default for s in payload.settings if s.label.startswith("category")]
    limit = [s.default for s in payload.settings if s.label.startswith("limit")]
    events=await EventService.get_formatted_events(
        city[0], 
        "", # remove this line 
        category[0], 
        limit[0]
    )
    json ={
        "message": str(events),
        "username": "Local Notifier",
        "event_name": "Notifier Event",
        "status": "error"}
    
    async with httpx.AsyncClient() as client:
        response=await client.post(Config.TELEX_WEBHOOK_URL, json=json)
        logger.info(f"Successfully sent events to Telex: {response.text}")
 
    return json

