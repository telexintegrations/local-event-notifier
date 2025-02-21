import logging

import aiohttp

from app.config import Config

api_key = Config.TICKET_MASTER_API_KEY
api_url = Config.TICKET_MASTER_API_URL
logger = logging.getLogger(__name__)


class EventRepository:
    """
    Fetches events from Ticketmaster API
    """

    @staticmethod
    async def fetch_events(city: str = None, category: str = None, limit: int = 5):
        params = {"apikey": api_key, "size": limit, "sort": "date,asc"}
        if city:
            params["city"] = city
        if category:
            params["classificationName"] = category

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, params=params) as response:
                if response.status != 200:
                    logger.error(f"Failed to fetch events: {response.status}")
                    return []

                data = await response.json()
                return data.get("_embedded", {}).get("events", [])
