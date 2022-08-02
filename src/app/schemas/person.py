from pydantic import BaseModel, HttpUrl
from typing import Sequence,Optional


class PersonBase(BaseModel):
    Id: int
    partyId: int
    firstName: Optional[str]
    lastName: Optional[str]
    nationalCode: Optional[str]
    


class PersonCreate(PersonBase):
    partyId: int
    firstName: Optional[str]
    lastName: Optional[str]
    nationalCode: Optional[str]
    


class PersonUpdate(PersonBase):
    partyId: int
    firstName: Optional[str]
    lastName: Optional[str]
    nationalCode: Optional[str]


# Properties shared by models stored in DB
class PersonInDBBase(PersonBase):


    class Config:
        orm_mode = True


# Properties to return to client
class Person(PersonInDBBase):
    pass


# Properties properties stored in DB
class PersonInDB(PersonInDBBase):
    pass


class PersonSearchResults(BaseModel):
    results: Sequence[Person]
