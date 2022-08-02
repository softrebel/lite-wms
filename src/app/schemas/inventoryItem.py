from typing import Optional,Sequence,List

from pydantic import BaseModel, EmailStr
from .inventoryItemDetail import InventoryItemDetail
from .party import Party
from .facility import Facility
from datetime import date

class InventoryItemBase(BaseModel):
    Id: int
    facilityId: Optional[int]
    partyId: Optional[int] = None
    party: Party
    facility:Facility
    inventoryItemDetails: List[InventoryItemDetail]=[]
    fromDate: Optional[date]
    


# Properties to receive via API on creation
class InventoryItemCreate(BaseModel):
    facilityId:Optional[int]
    partyId: Optional[int] = None
    fromDate: Optional[date]


# Properties to receive via API on update
class InventoryItemUpdate(InventoryItemBase):
    ...


class InventoryItemInDBBase(InventoryItemBase):
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class InventoryItem(InventoryItemInDBBase):
    pass


class InventoryItemSearchResults(BaseModel):
    results: Sequence[InventoryItem]


