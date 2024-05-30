from fastapi import APIRouter, HTTPException, Query
from database.models import Lot
from database.services import (
    create_lot,
    get_all_lots,
    get_lot,
    update_lot_values,
    delete_lot_from_db,
)
from database.schema import LotCreateSchema, LotUpdateSchema

router = APIRouter()


@router.get("/", response_model=list[Lot])
async def read_lots(offset: int = 0, limit: int = Query(default=100, le=100)):
    return get_all_lots(offset, limit)


@router.post("/", status_code=201, response_model=Lot)
async def insert_lot(lot: LotCreateSchema):
    lot = Lot.model_validate(lot)
    create_lot(lot)
    return lot


@router.get("/{lot_id}", response_model=Lot)
async def read_lot(lot_id: int):
    response = get_lot(lot_id)
    if not response:
        raise HTTPException(status_code=404, detail="No Lot with this id!")
    return response


@router.put("/{lot_id}", response_model=Lot)
async def update_lot(lot_id: int, data: LotUpdateSchema):
    lot = get_lot(lot_id)
    if not get_lot(lot_id):
        raise HTTPException(status_code=404, detail="No Lot with this id!")
    return update_lot_values(lot, data.model_dump(exclude_unset=True))


@router.delete("/{lot_id}")
async def delete_lot(lot_id: int):
    lot = get_lot(lot_id)
    if not get_lot(lot_id):
        raise HTTPException(status_code=404, detail="No Lot with this id!")
    return delete_lot_from_db(lot)
