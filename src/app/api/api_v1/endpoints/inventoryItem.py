from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.inventoryItem import InventoryItem, InventoryItemCreate,InventoryItemSearchResults

router = APIRouter()



@router.get("/", status_code=200, response_model=InventoryItemSearchResults)
def search_partys(
    *,
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:

    results = crud.inventoryItem.get_multi(db=db, limit=max_results)
    return {"results": list(results)[:max_results]}

@router.get("/facility/{facilityId}", status_code=200, response_model=InventoryItemSearchResults)
def search_partys(
    *,
    facilityId: int,
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:

    results = crud.inventoryItem.get_by_facility_id(db=db,facilityId=facilityId, limit=max_results)
    return {"results": list(results)[:max_results]}

