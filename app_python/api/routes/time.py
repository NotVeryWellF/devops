from fastapi import APIRouter, HTTPException
from aiohttp_requests import requests

router = APIRouter()


@router.get("/moscow")
async def moscow_time() -> str:
    """Endpoint of the Moscow time (proxy of the timeapi.io API for the time)"""
    time_response = await requests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Moscow")
    time = await time_response.json()
    if time_response.status == 200:
        return time
    else:
        raise HTTPException(status_code=404, detail="Not found")
