from fastapi import APIRouter

from app.api.routes import ai, files, health

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(ai.router)
api_router.include_router(files.router)
