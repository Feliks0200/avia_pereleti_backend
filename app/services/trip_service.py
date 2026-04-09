from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Trip


class TripService:
    @staticmethod
    async def create_trip(db:AsyncSession,data):
        trip = Trip(**data.dict())
        db.add(trip)
        await db.commit()
        return trip
    @staticmethod
    async def get_trip(db: AsyncSession,from_city:str|None=None,to_city:str|None=None):
        result_f = select(Trip)
        if from_city:
            result_f = result_f.where(Trip.from_city == from_city)
        if to_city:
            result_f = result_f.where(Trip.to_city == to_city)
        results = await db.execute(result_f)
        return results.scalars().all()
    @staticmethod
    async def get_by_id(db:AsyncSession,trip_id:int):
        result = await  db.execute(select(Trip).where(Trip.id == trip_id))
        return result.scalar_one_or_none()
    @staticmethod
    async def update_trip(db:AsyncSession,trip_id:int,data:dict): # <-- обновление трипа
        result = await db.execute(select(Trip).where(Trip.id == trip_id))
        trip = result.scalar_one_or_none()
        if not trip: # <-- если нету то нилл
            return None
        if data.from_city is not None: # <-- проверка заполнен ли
            trip.from_city = data.from_city
        if data.to_city is not None: # <-- проверка заполнен ли
            trip.to_city = data.to_city
        if data.price is not None: # <-- проверка заполнен ли
            trip.price = data.price
        await db.commit()
        await db.refresh(trip)
        return trip

    @staticmethod
    async def delete_trip(db:AsyncSession, trip_id:int):
        result = await db.execute(select(Trip).where(Trip.id == trip_id))
        trip = result.scalar_one_or_none()
        if not trip:
            return None
        await db.delete(trip)
        await db.commit()
        return trip