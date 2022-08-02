from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


InventoryItem=Base.classes.InventoryItem
InventoryItem.inventoryItemDetails = relationship("InventoryItemDetail")
