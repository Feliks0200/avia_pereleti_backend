from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.trip import TripCreate
from app.services.trip_service import TripService
from database import get_db

trips_router = APIRouter(prefix="/trips", tags=["trips"])

# @trips_router.post("/")
# async def create_trip(from_city:str,to_city:str,price:float,db:AsyncSession=Depends(get_db)):
#     return await TripService.create_trip(db,from_city,to_city,price)

@trips_router.get("/") # <-- получение всех билетов
async def get_trips(from_city:str|None=None,to_city:str|None=None,db:AsyncSession=Depends(get_db)):
    return await TripService.get_trip(db,from_city,to_city)

# @trips_router.get("/")
# async def get_trip(db:AsyncSession=Depends(get_db)):
#     return await TripService.get_trip(db)

@trips_router.get("/{trip_id}") # <-- получение твоего билета
async def get_trip_id(trip_id:int,db:AsyncSession=Depends(get_db)):
    trip = await TripService.get_by_id(db,trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

