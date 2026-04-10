from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import User


class UserService:
    @staticmethod
    async def create_user(db:AsyncSession,data): # <-- создание пользователя
        user = User(**data.dict()) # <-- получение словаря
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    @staticmethod
    async def login(db:AsyncSession,email:str,password:str): # <-- логин пользователя
        result = await db.execute(select(User).where(User.email == email,User.password == password))
        user = result.scalar_one_or_none()
        if not user or user.password != password:
            return None
        return user 
    @staticmethod
    async def get_user_by_id(db:AsyncSession,user_id:int): # <-- получение пользователя по id
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    @staticmethod
    async def get_user_all(db:AsyncSession): # <-- получение всех пользователей
        result = await db.execute(select(User))
        return result.scalars().all()
    @staticmethod
    async def update_user(db:AsyncSession,user_id:int,data): # <-- обновление инфы о пользователе
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return None
        if data.email != None:
            user.email = data.email
        if data.password != None:
            user.password = data.password
        if data.full_name != None:
            user.full_name = data.full_name
        if data.phone != None:
            data.phone = data.phone
        await db.commit()
        await db.refresh(user)
        return user
    @staticmethod
    async def delete_user(db:AsyncSession,user_id:int): # <--удалениеи пользователя
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return None
        await db.delete(user)
        await db.commit()
        return user
