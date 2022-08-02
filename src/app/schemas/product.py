from typing import Optional,Sequence

from pydantic import BaseModel, EmailStr
from .unitOfMeasure import UnitOfMeasure

class ProductBase(BaseModel):
    Id: int
    name: Optional[str]
    subtype : int
    description: Optional[str]
    unitOfMeasureId:int
    unitofmeasure:Optional[UnitOfMeasure]

# Properties to receive via API on creation
class ProductCreate(ProductBase):
    name: Optional[str]
    subtype : int
    description: Optional[str]
    unitOfMeasureId:int
    unitofmeasure:Optional[UnitOfMeasure]


# Properties to receive via API on update
class ProductUpdate(ProductBase):
    ...


class ProductInDBBase(ProductBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Product(ProductInDBBase):
    pass

class ProductQuantity(ProductInDBBase):
    name: str
    sum : int
class ProductQuantityResults(ProductInDBBase):
    results: Sequence[ProductQuantity]

