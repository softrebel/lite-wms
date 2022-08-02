from pydantic import BaseModel,HttpUrl

from typing import Sequence


class UnitOfMeasureBase(BaseModel):
    Id: int
    abbreviation: str
   


class UnitOfMeasureCreate(UnitOfMeasureBase):
    abbreviation: str
    


class UnitOfMeasureUpdate(UnitOfMeasureBase):
    ...


# Properties shared by models stored in DB
class UnitOfMeasureInDBBase(UnitOfMeasureBase):
   
    class Config:
        orm_mode = True


# Properties to return to client
class UnitOfMeasure(UnitOfMeasureInDBBase):
    pass


# Properties properties stored in DB
class UnitOfMeasureInDB(UnitOfMeasureInDBBase):
    pass


class UnitOfMeasureSearchResults(BaseModel):
    results: Sequence[UnitOfMeasure]
