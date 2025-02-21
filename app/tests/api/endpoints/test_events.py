import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_events_success(client: AsyncClient):
    """
    Test fetching events successfully
    """
    response = await client.get(
        "/events", params={"city": "Hamburg", "category": "music", "limit": 3}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_events_missing_params(client: AsyncClient):
    """
    Test fetching events with missing optional parameters
    """
    response = await client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_integration_json(client: AsyncClient):
    """
    Test fetching integration JSON
    """
    response = await client.get("/integration.json")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.asyncio
async def test_post_tick_success(client: AsyncClient):
    """
    Test successful tick event posting
    """
    payload = {
        "settings": [
            {"label": "city", "default": "Berlin"},
            {"label": "category", "default": "sports"},
            {"label": "limit", "default": 5},
        ]
    }
    response = await client.post("/tick", json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert "message" in response_data
    assert response_data["status"] == "success"


@pytest.mark.asyncio
async def test_post_tick_missing_settings(client: AsyncClient):
    """
    Test tick event posting with missing settings
    """
    payload = {"settings": []}
    response = await client.post("/tick", json=payload)
    assert response.status_code == 422
