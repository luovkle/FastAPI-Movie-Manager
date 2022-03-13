from fastapi import APIRouter

from app.api.api_v1.endpoints.films import router as films_router

api_router = APIRouter()
api_router.include_router(films_router, prefix="/films", tags=["Films"])
