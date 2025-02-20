from fastapi import FastAPI
import httpx

print("hello")
app = FastAPI()
async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
@app.get("/data")
async def get_data():
    data_url = "https://www.eventbriteapi.com/v3/events/{event_id}/?expand=ticket_classes"
    data = await fetch_data(data_url)
    print(data)
    return {"data": data}