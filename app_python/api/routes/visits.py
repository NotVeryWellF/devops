from fastapi import APIRouter, Request
import aiofiles
import datetime

router = APIRouter(tags=["visits"])


@router.get("/visits")
async def get_visits() -> str:
    try:
        async with aiofiles.open('app_python/visits/visits.txt', mode='r') as f:
            visits = await f.read()
        return visits
    except Exception as e:
        print(e)
        return ""


@router.get("/")
async def visit(req: Request) -> None:
    async with aiofiles.open("app_python/visits/visits.txt", mode="a") as f:
        await f.write(f"Client: {req.client.host} visited site at {datetime.datetime.now()}\n")
