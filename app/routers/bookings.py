from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate
from app.services.booking_service import BookingService
from database import get_db

book_router = APIRouter(prefix="/bookings", tags=["bookings"])

@book_router.post("/")
async def create_booking(data:BookingCreate,db:AsyncSession=Depends(get_db)):
    return await BookingService.create_booking(db,data)
@book_router.get("/")
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingService.get_booking(db)
