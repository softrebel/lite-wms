from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.facility import Facility, FacilityCreate,FacilitySearchResults

router = APIRouter()



@router.get("", status_code=200, response_model=FacilitySearchResults)
def search_partys(
    *,
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:

    results = crud.facility.get_multi(db=db, limit=max_results)
    return {"results": list(results)[:max_results]}

