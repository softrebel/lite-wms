from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


InventoryItemDetail=Base.classes.InventoryItemDetail
InventoryItemDetail.InventoryItemStatusType=InventoryItemDetail.inventoryitemstatustype
print('slm')