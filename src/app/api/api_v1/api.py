from fastapi import APIRouter

from app.api.api_v1.endpoints import party,facility,inventoryItem


api_router = APIRouter()
api_router.include_router(party.router, prefix="/party", tags=["party"])
api_router.include_router(facility.router, prefix="/facility", tags=["facility"])
api_router.include_router(inventoryItem.router, prefix="/inventory_item", tags=["inventoryItem"])
