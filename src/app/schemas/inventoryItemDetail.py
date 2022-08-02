from typing import Optional,Sequence

from pydantic import BaseModel, EmailStr
# from .inventoryItem import InventoryItem
from .container import Container
from .product import Product
from .inventoryItemStatusType import InventoryItemStatusType
class InventoryItemDetailBase(BaseModel):
    Id: int
    serialNumber: Optional[str]
    quantity: int
    inventoryItemId:int
    # inventoryItem : InventoryItem
    containerId:int
    container: Optional[Container]
    productId: int
    product : Optional[Product]
    inventoryItemStatusTypeId: Optional[int]
    inventoryitemstatustype: Optional[InventoryItemStatusType]



# Properties to receive via API on creation
class InventoryItemDetailCreate(BaseModel):
    serialNumber: Optional[str]
    quantity: Optional[int]
    inventoryItemId:Optional[int]
    containerId:Optional[int]
    productId: Optional[int]
    inventoryItemStatusTypeId: Optional[int]


# Properties to receive via API on update
class InventoryItemDetailUpdate(InventoryItemDetailBase):
    ...


class InventoryItemDetailInDBBase(InventoryItemDetailBase):
    Id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class InventoryItemDetail(InventoryItemDetailInDBBase):
    pass


class InventoryItemDetailSearchResults(BaseModel):
    results: Sequence[InventoryItemDetail]