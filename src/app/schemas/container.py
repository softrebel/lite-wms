from pydantic import BaseModel, HttpUrl

from typing import Sequence


class ContainerBase(BaseModel):
    Id: int
    name: str
    facilityId: int
    


class ContainerCreate(ContainerBase):
    Id: int
    name: str
    facilityId: int
    


class ContainerUpdate(ContainerBase):
    name: str
    facilityId: int


# Properties shared by models stored in DB
class ContainerInDBBase(ContainerBase):
    Id: int
    name: str
    facilityId: int

    class Config:
        orm_mode = True


# Properties to return to client
class Container(ContainerInDBBase):
    pass


# Properties properties stored in DB
class ContainerInDB(ContainerInDBBase):
    pass


class ContainerSearchResults(BaseModel):
    results: Sequence[Container]
