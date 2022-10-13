from fastapi import APIRouter

from app.api import echo, monitoring

api_router = APIRouter()

api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(monitoring.router, tags=["info"])
