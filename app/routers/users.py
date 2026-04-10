from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.user import UserUpdate
from app.services.user_service import UserService
from database import get_db

user_router = APIRouter(prefix="/users",tags=["Users"])
@user_router.get("/me/{user_id}") # <-- получение своего профиля
async def get_me(user_id:int,db:AsyncSession=Depends(get_db)):
    user=await UserService.get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user
@user_router.put("/me/{user_id}") # <-- обновление инфы о пользователе
async def update_user(user_id:int,data:UserUpdate,db:AsyncSession=Depends(get_db)):
    user = await UserService.update_user(db,user_id,data)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return {
        "message" : "Profile updated successfully",
        "user" : user
    }