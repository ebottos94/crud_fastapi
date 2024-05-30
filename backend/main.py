from fastapi import FastAPI
from routers.lot import router as LotRouter

app = FastAPI()

app.include_router(LotRouter, tags=["Lot"], prefix="/api/lot")
