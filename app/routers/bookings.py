
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate
from app.services.booking_service import BookingService
from database import get_db

book_router = APIRouter(prefix="/bookings", tags=["bookings"])

@book_router.post("/") # <-- создание брони
async def create_booking(data:BookingCreate,db:AsyncSession=Depends(get_db)):
    booking = await BookingService.create_booking(db,data)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@book_router.get("/") # <-- получение брони
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingService.get_booking(db)

@book_router.delete("/bookings/{booking_id}") # <-- получение брони по id
async def delete_booking(booking_id:int,db:AsyncSession=Depends(get_db)):
    booking = await BookingService.delete_booking(db,booking_id)
    if not booking:
        raise HTTPException(status_code=404,detail="Booking not found")
    return {"message":"Booking cancelled","booking":booking}


@book_router.get("/user/{user_id}") # <--получение брони юзера по id
async def get_user_booking(user_id:int,db:AsyncSession=Depends(get_db)):
    return await BookingService.get_user_bookings(db,user_id)

@book_router.post("/{booking_id}/pay") # <-- оплата брони
async def pay_booking(booking_id:int,db:AsyncSession=Depends(get_db)):
    booking = await BookingService.pay_booking(db,booking_id)
    if not booking:
        raise HTTPException(status_code=404,detail="Booking not found")
    return {"message":"Booking paid","booking":booking}