import httpx
import logging
from app.config import Config

logger = logging.getLogger(__name__)

class TelexService:
    """
    Sends event notifications to Telex using a webhook URL. Takes a channel ID.
    """

    @staticmethod
    async def send_to_telex(channel_id: str, events: list):
        """
        Send event data to Telex webhook
        """
        if not Config.TELEX_WEBHOOK_URL:
            logger.error("Telex webhook URL is not configured!")
            return

        payload = {
            "channel_id": channel_id,  # Telex requires a channel ID
            "events": events
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(Config.TELEX_WEBHOOK_URL, json=payload)
                response.raise_for_status()
                logger.info(f"Successfully sent events to Telex: {response.status_code}")
        except httpx.HTTPStatusError as e:
            logger.error(f"Error sending events to Telex: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
