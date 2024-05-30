from .db import engine
from .models import Lot
from sqlmodel import Session, select


def create_lot(lot: Lot):
    with Session(engine) as session:
        session.add(lot)
        session.commit()
        session.refresh(lot)
        return lot


def get_all_lots(offset: int, limit: int):
    statement = select(Lot).offset(offset).limit(limit)
    with Session(engine) as session:
        return session.exec(statement).all()


def get_lot(lot_id: int):
    with Session(engine) as session:
        return session.get(Lot, lot_id)


def update_lot_values(lot: Lot, data: dict):
    with Session(engine) as session:
        lot.sqlmodel_update(data)
        session.add(lot)
        session.commit()
        session.refresh(lot)
        return lot


def delete_lot_from_db(lot: Lot):
    with Session(engine) as session:
        session.delete(lot)
        session.commit()
        return {"deleted": True}
