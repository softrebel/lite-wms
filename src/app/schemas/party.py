from pydantic import BaseModel, HttpUrl

from typing import Sequence,List,Optional
from .person import Person
from .company import Company

class PartyBase(BaseModel):
    Id: int
    typeId: int
    person: Optional[List[Person]]
    company: Optional[List[Company]]

    


class PartyCreate(PartyBase):
    typeId: int
    


class PartyUpdate(PartyBase):
    typeId: int


# Properties shared by models stored in DB
class PartyInDBBase(PartyBase):

    class Config:
        orm_mode = True


# Properties to return to client
class Party(PartyInDBBase):
    pass


# Properties properties stored in DB
class PartyInDB(PartyInDBBase):
    pass


class PartySearchResults(BaseModel):
    results: Sequence[Party]

class PartyViewModel(PartyInDBBase):
    Id: Optional[int]
    typeId: Optional[int]
    person: Optional[List[Person]]
    company: Optional[List[Company]]
    name:Optional[str]