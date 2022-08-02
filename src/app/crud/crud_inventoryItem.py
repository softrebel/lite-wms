from app.crud.base import CRUDBase
from app.models.inventoryItem import InventoryItem
from app.schemas.inventoryItem import InventoryItemCreate, InventoryItemUpdate
from sqlalchemy.orm import Session
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder

class CRUDInventoryItem(CRUDBase[InventoryItem, InventoryItemCreate, InventoryItemUpdate]):
    def get_by_facility_id(
        self, db: Session, *,facilityId:int, skip: int = 0, limit: int = 100
    ) -> List[InventoryItem]:
        return db.query(InventoryItem).filter(InventoryItem.facilityId==facilityId).order_by(InventoryItem.Id).offset(skip).limit(limit).all()
    
    def get_between_dates(
        self, db: Session, *, fromDate=None,thruDate=None, skip: int = 0, limit: int = 100
    ) -> List[InventoryItem]:
        query=db.query(self.model)
        if fromDate :
            query=query.filter(InventoryItem.fromDate>=fromDate)
        if thruDate :
            query=query.filter(InventoryItem.fromDate<=thruDate)
        return query.order_by(self.model.Id).offset(skip).limit(limit).all()


inventoryItem = CRUDInventoryItem(InventoryItem)
