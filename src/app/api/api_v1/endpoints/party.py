from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.party import Party, PartyCreate, PartySearchResults

router = APIRouter()


@router.get("/{party_id}", status_code=200, response_model=Party)
def fetch_party(
    *,
    party_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single party by ID
    """
    result = crud.party.get(db=db, id=party_id)
    if not result:

        raise HTTPException(
            status_code=404, detail=f"Party with ID {party_id} not found"
        )

    return result


@router.get("/search/", status_code=200, response_model=PartySearchResults)
def search_partys(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for partys based on label keyword
    """
    partys = crud.party.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": partys}

    results = filter(lambda party: keyword.lower() in party.label.lower(), partys)
    return {"results": list(results)[:max_results]}


@router.post("/", status_code=201, response_model=Party)
def create_party(
    *, party_in: PartyCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new party in the database.
    """
    party = crud.party.create(db=db, obj_in=party_in)

    return party
