from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from database import get_db

admin_router = APIRouter(prefix="/admin",tags=["Admin"])
async def check_admin(db:AsyncSession,admin_id:int):
    admin = await UserService.get_user_by_id(db,admin_id)
    if not admin or admin.role!="admin": # <-- это сервис должен был быть. но ради него одного в падлу создавать новый файл. поэтому он тут
        return None
    return admin

@admin_router.get("/users")
async def get_users(admin_id:int,db:AsyncSession = Depends(get_db())): # <-- Depends не забывать главное!
    admin = await check_admin(db,admin_id) # <-- проверка на админа
    if not admin:
        raise HTTPException(status_code=404,detail="Admin not found")
    return await UserService.get_user_all(db) # <-- если ты админ тебе всех челиков вернут