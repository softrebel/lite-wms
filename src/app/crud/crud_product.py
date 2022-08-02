from typing import Any, Dict, Optional, Union,List,Tuple

from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.crud.base import CRUDBase
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    
    def get_quantity_by_facility(self,db:Session,*,facilityId:int)->List[Tuple]:
        statement = text("""
        SELECT p.name,b.sum,uom.abbreviation FROM product p INNER JOIN UnitOfMeasure uom ON p.unitOfMeasureId = uom.Id LEFT JOIN (
        SELECT productId, SUM(iid.quantity) AS 'sum' FROM InventoryItemDetail iid INNER JOIN InventoryItem ii ON iid.inventoryItemId = ii.Id
        WHERE ii.facilityId=:facilityId
        GROUP BY iid.productId 
        ) b ON b.productId=p.id 
        """)
        rs = db.execute(statement, params={'facilityId':facilityId})
        return rs.fetchall()

    

product = CRUDProduct(Product)
