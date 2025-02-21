import logging

import httpx

from app.config import Config
from app.models.events import Event
from app.repositories.events import EventRepository

logger = logging.getLogger(__name__)


class EventService:
    @staticmethod
    async def get_formatted_events(
        city: str = None, category: str = None, limit: int = 5
    ):
        logger.info(f"Fetching events for city={city}, category={category}")
        events = await EventRepository.fetch_events(city, category, limit)

        if not events:
            logger.warning("No events found")
            return []

        formatted_events = [
            Event(
                title=event.get("name", "Unknown Event"),
                url=event.get("url", "#"),
                start_time=event.get("dates", {})
                .get("start", {})
                .get("localDate", "TBA"),
                venue=event.get("_embedded", {})
                .get("venues", [{}])[0]
                .get("name", "TBA"),
            ).dict()
            for event in events
        ]

        logger.info(f"Successfully fetched {len(formatted_events)} events")

        # Send events to Telex
        await EventService.send_to_telex(formatted_events)

        return formatted_events

    @staticmethod
    async def send_to_telex(events):
        """
        Send event data to Telex webhook
        """
        if not Config.TELEX_WEBHOOK_URL:
            logger.error("Telex webhook URL is not configured!")
            return

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    Config.TELEX_WEBHOOK_URL, json={"events": events}
                )
                response.raise_for_status()
                logger.info(
                    f"Successfully sent events to Telex: {response.status_code}"
                )
        except httpx.HTTPStatusError as e:
            logger.error(
                f"Error sending events to Telex: {e.response.status_code} - {e.response.text}"
            )
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
