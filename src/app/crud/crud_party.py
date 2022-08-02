from app.crud.base import CRUDBase
from app.models.party import Party
from app.schemas.party import PartyCreate, PartyUpdate,PartyViewModel
from sqlalchemy.orm import Session
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

class CRUDParty(CRUDBase[Party, PartyCreate, PartyUpdate]):
    def get_with_names(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[PartyViewModel]:
        res= self.get_multi(db)
        out=[]
        for item in res:
            temp=PartyViewModel()
            temp.Id=item.Id
            temp.typeId=item.typeId
            temp.person=item.person
            temp.company=item.company
            if item.typeId==1:
                temp.name=f'{item.person[0].firstName} {item.person[0].lastName}'
            elif item.typeId==2:
                temp.name=item.company[0].title
            out.append(temp)
        return out



party = CRUDParty(Party)
