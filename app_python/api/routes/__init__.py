from .time import router as time_router
from fastapi import APIRouter

# Collect all the routes in one place
router = APIRouter()
router.include_router(time_router, prefix="/time")
