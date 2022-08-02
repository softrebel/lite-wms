from typing import Optional,Sequence

from pydantic import BaseModel, EmailStr
from .container import Container
from .product import Product
class InventoryItemStatusTypeBase(BaseModel):
    Id: int
    name: str
    



# Properties to receive via API on creation
class InventoryItemStatusTypeCreate(InventoryItemStatusTypeBase):
    Id: int
    name: str


# Properties to receive via API on update
class InventoryItemStatusTypeUpdate(InventoryItemStatusTypeBase):
    ...


class InventoryItemStatusTypeInDBBase(InventoryItemStatusTypeBase):
    Id: int
    name: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class InventoryItemStatusType(InventoryItemStatusTypeInDBBase):
    pass


class InventoryItemStatusTypeSearchResults(BaseModel):
    results: Sequence[InventoryItemStatusType]