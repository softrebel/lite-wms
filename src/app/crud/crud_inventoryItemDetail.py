from app.crud.base import CRUDBase
from app.models.inventoryItemDetail import InventoryItemDetail
from app.schemas.inventoryItemDetail import InventoryItemDetailCreate, InventoryItemDetailUpdate


class CRUDInventoryItemDetail(CRUDBase[InventoryItemDetail, InventoryItemDetailCreate, InventoryItemDetailUpdate]):
    ...


inventoryItemDetail = CRUDInventoryItemDetail(InventoryItemDetail)
