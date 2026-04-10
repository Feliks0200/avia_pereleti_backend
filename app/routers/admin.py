from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate
from app.schemas.trip import TripCreate
from app.services.booking_service import BookingService
from app.services.trip_service import TripService
from app.services.user_service import UserService
from database import get_db

admin_router = APIRouter(prefix="/admin",tags=["admin"])

async def check_admin(db:AsyncSession,admin_id:int):
    admin = await UserService.get_user_by_id(db,admin_id)
    if not admin or admin.role != "admin":# <-- это сервис должен был быть. но ради него одного в падлу создавать новый файл. поэтому он тут
        print(admin.role)
        return None
    return admin

@admin_router.get("/users") # <-- получение всех пользователей
async def get_users(admin_id:int,db:AsyncSession = Depends(get_db)): # <-- Depends не забывать главное!
    admin = await check_admin(db,admin_id) # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404,detail="Admin not found")
    return await UserService.get_user_all(db) # <-- если ты админ тебе всех челиков вернут

@admin_router.get("/users/{user_id}") # <-- получение пользователя
async def get_user(admin_id:int,user_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)  # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    users = await UserService.get_user_by_id(db,user_id) # <-- получение пользователя
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users # <-- если ты админ тебе одного вернут

@admin_router.delete("/users/{user_id}") # <-- удаление пользователя
async def delete_user(admin_id:int,user_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id) # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    users = await UserService.delete_user(db, user_id) # <-- получение и удаление пользователя
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message":"User deleted successfully"}

@admin_router.post("/trips") # <-- создание трипа
async def create_trips(admin_id:int,trip:TripCreate,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)  # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return await TripService.create_trip(db,trip) # <-- создание трипа

@admin_router.put("/trips/{trip_id}") # <-- обновление трипа
async def update_trips(admin_id:int,data:TripCreate,trip_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id) # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    trip = await TripService.update_trip(db,trip_id,data)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message":"Trip Update","Trip":trip} # кстати я на паре 09.04.2026 фулл пару играл в Bite By Night :3

@admin_router.delete("/trips/{trip_id}") # <-- удаление трипа
async def delete_trips(admin_id:int,trip_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    trip = TripService.delete_trip(db, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message":"Trip Deleted"}

@admin_router.get("/bookings") # <-- получение всех броней
async def get_all_bookingss(admin_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return await BookingService.get_booking(db)

@admin_router.get("/bookings/{booking_id}") # <-- получение брони по id
async def get_id_book(admin_id:int,booking_id:int,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    book = await BookingService.get_user_bookings(db, booking_id)
    if not book:
        raise HTTPException(status_code=404, detail="Booking not found")
    return book

@admin_router.put("/bookings/{booking_id}") # <-- изменение бронии
async def izm_book(admin_id:int,booking_id:int,data:BookingCreate,db:AsyncSession = Depends(get_db)):
    admin = await check_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    books = await BookingService.adm_update_booking(db,booking_id,data)
    if not books:
        raise HTTPException(status_code=404, detail="Booking not found")
    return books