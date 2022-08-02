from pathlib import Path
from typing import Any, Optional
from fastapi import FastAPI, APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.schemas.inventoryItem import InventoryItemCreate
from app.schemas.inventoryItemDetail import InventoryItemDetailCreate
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

root_router = APIRouter()
app = FastAPI(title="Recipe API")


@root_router.get("/", status_code=200)
def root(
    request: Request,
    db: Session = Depends(deps.get_db),
    fromDate:str=None,
    thruDate:str=None
) -> dict:
    """
    Root GET
    """
    
    parties = crud.party.get_multi(db=db, limit=10)
    inventoryItems=crud.inventoryItem.get_between_dates(db,fromDate=fromDate,thruDate=thruDate)
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "parties": parties,'inventoryItems':inventoryItems,'fromDate':fromDate,'thruDate':thruDate},
    )


@root_router.get("/add", status_code=200)
def add(
    request: Request,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Add GET
    """
    parties = crud.party.get_with_names(db=db)
    products = crud.product.get_multi(db)
    status_types=crud.inventoryItemStatusType.get_multi(db)
    facilities=crud.facility.get_multi(db)
    containers=crud.container.get_multi(db)
    return TEMPLATES.TemplateResponse(
        "add.html",
        {"request": request, "parties": parties,'products':products,'status_types':status_types,'facilities':facilities,'containers':containers,"msg":None},
    )


@root_router.post("/add", status_code=200)
def add(
    request: Request,
    facilityId:int=Form(),
    containerId:int=Form(),
    partyId:int=Form(),
    productId:int=Form(),
    fromDate:str=Form(),
    quantity:int=Form(),
    inventoryItemStatusTypeId:int=Form(),
    serialNumber:str=Form(None),
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Add GET
    """
    msg = None
    def return_add():
        parties = crud.party.get_with_names(db=db)
        
        products = crud.product.get_multi(db)
        status_types=crud.inventoryItemStatusType.get_multi(db)
        facilities=crud.facility.get_multi(db)
        containers=crud.container.get_multi(db)
        return TEMPLATES.TemplateResponse(
            "add.html",
            {"request": request, "parties": parties,'products':products,'status_types':status_types,'facilities':facilities,'containers':containers,"msg":msg},
        )
    if not facilityId:
        msg='انبار را مشخص کنید'
        return return_add()
    if not containerId:
        msg='قفسه را مشخص کنید'
        return return_add()
    if not productId:
        msg='کالا را مشخص کنید'
        return return_add()
    if not inventoryItemStatusTypeId:
        msg='ورود/خروج را مشخص کنید'
        return return_add()
    if not quantity:
        msg='تعداد را مشخص کنید'
        return return_add()
    if not fromDate:
        msg='زمان را مشخص کنید'
        return return_add()
    if not partyId:
        msg='طرف حساب را مشخص کنید'
        return return_add()
    try:
        item=InventoryItemCreate()
        item.facilityId=facilityId
        item.partyId=partyId
        item.fromDate=fromDate
        item=crud.inventoryItem.create(db=db,obj_in=item)
        detail=InventoryItemDetailCreate()
        detail.inventoryItemId=item.Id
        detail.containerId=containerId
        detail.inventoryItemStatusTypeId=inventoryItemStatusTypeId
        if inventoryItemStatusTypeId == 1:
            detail.quantity=quantity
        elif inventoryItemStatusTypeId == 2:
            detail.quantity=quantity * -1
        detail.productId=productId
        detail.serialNumber=serialNumber
        detail=crud.inventoryItemDetail.create(db=db,obj_in=detail)
        db.commit()
        msg='عملیات با موفقیت انجام شد'
        return return_add()
    except:
        db.rollback()
        return return_add()
    

    
    



@root_router.get('/report',status_code=200)
def report(request:Request, 
        db:Session=Depends(deps.get_db),
        facilityId: Optional[int] = 1,
    ) -> dict:
    """
    Report GET
    """
    facilities=crud.facility.get_multi(db)
    result=crud.product.get_quantity_by_facility(db,facilityId=facilityId)
    facility=crud.facility.get(db, id=facilityId)
    return TEMPLATES.TemplateResponse(
        "product_report.html",
        {"request": request, "result": result,"facility":facility,'facilities':facilities},
    )



app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
