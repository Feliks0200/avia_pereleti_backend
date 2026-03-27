from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Trip


class TripService:
    @staticmethod
    async def create_trip(db:AsyncSession,from_city:str,to_city:str,price:float):
        trip = Trip(from_city=from_city,to_city=to_city,price=price)
        db.add(trip)
        await db.commit()
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