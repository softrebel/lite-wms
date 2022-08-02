from pydantic import BaseModel, HttpUrl

from typing import Sequence


class FacilityBase(BaseModel):
    Id: int
    name: str
    


class FacilityCreate(FacilityBase):
    Id: int
    name: str
    


class FacilityUpdate(FacilityBase):
    name: str


# Properties shared by models stored in DB
class FacilityInDBBase(FacilityBase):
    Id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Facility(FacilityInDBBase):
    pass


# Properties properties stored in DB
class FacilityInDB(FacilityInDBBase):
    pass


class FacilitySearchResults(BaseModel):
    results: Sequence[Facility]
