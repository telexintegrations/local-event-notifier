import os

from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file


class Config:
    TICKET_MASTER_API_KEY = os.getenv("TICKET_MASTER_API_KEY")
    TELEX_WEBHOOK_URL = os.getenv("TELEX_WEBHOOK_URL")
    TICKET_MASTER_API_URL = os.getenv("TICKET_MASTER_API_URL")
