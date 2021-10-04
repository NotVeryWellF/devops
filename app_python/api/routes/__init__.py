from .time import router as time_router
from fastapi import APIRouter
from .visits import router as visits_router

# Collect all the routes in one place
router = APIRouter()
router.include_router(time_router, prefix="/api/time")
router.include_router(visits_router)
