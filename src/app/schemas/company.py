from pydantic import BaseModel, HttpUrl

from typing import Sequence,Optional


class CompanyBase(BaseModel):
    Id: int
    partyId: int
    title: Optional[str]
    nationalCode: Optional[str]
    


class CompanyCreate(CompanyBase):
    partyId: int
    title: Optional[str]
    nationalCode: Optional[str]
    


class CompanyUpdate(CompanyBase):
    partyId: int
    title: Optional[str]
    nationalCode: Optional[str]


# Properties shared by models stored in DB
class CompanyInDBBase(CompanyBase):

    class Config:
        orm_mode = True


# Properties to return to client
class Company(CompanyInDBBase):
    pass


# Properties properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass


class CompanySearchResults(BaseModel):
    results: Sequence[Company]
