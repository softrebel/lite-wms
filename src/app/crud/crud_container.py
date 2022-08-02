from app.crud.base import CRUDBase
from app.models.container import Container
from app.schemas.container import ContainerCreate, ContainerUpdate


class CRUDContainer(CRUDBase[Container, ContainerCreate, ContainerUpdate]):
    ...


container = CRUDContainer(Container)
