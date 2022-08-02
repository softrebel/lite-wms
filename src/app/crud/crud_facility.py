from app.crud.base import CRUDBase
from app.models.facility import Facility
from app.schemas.facility import FacilityCreate, FacilityUpdate


class CRUDFacility(CRUDBase[Facility, FacilityCreate, FacilityUpdate]):
    ...


facility = CRUDFacility(Facility)
