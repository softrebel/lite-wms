from app.crud.base import CRUDBase
from app.models.inventoryItemStatusType import InventoryItemStatusType
from app.schemas.inventoryItemStatusType import InventoryItemStatusTypeCreate,InventoryItemStatusTypeUpdate


class CRUDInventoryItemStatusType(CRUDBase[InventoryItemStatusType, InventoryItemStatusTypeCreate, InventoryItemStatusTypeUpdate]):
    ...


inventoryItemStatusType = CRUDInventoryItemStatusType(InventoryItemStatusType)
