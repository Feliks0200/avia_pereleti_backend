from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Booking, User, Trip


class BookingService:
    @staticmethod
    async def create_booking(db: AsyncSession, data):
        user_result = await db.execute(select(User).where(User.id == data.user_id))
        user = user_result.scalar_one_or_none()
        if not user:
            return None
        trips_result = await db.execute(select(Trip).where(Trip.id == data.trip_id))
        trip = trips_result.scalar_one_or_none()
        if not trip:
            return None
        booking = Booking(**data.dict())
        db.add(booking)
        await db.commit()
        await db.refresh(booking)
        return booking
    @staticmethod
    async def get_booking(db:AsyncSession):
        bookings = await db.execute(select(Booking))
        return bookings.scalars().all()
    @staticmethod
    async def delete_booking(db:AsyncSession,booking_id:int):
        result = await db.execute(select(Booking).where(Booking.id==booking_id))
        booking = result.scalar_one_or_none()
        if not booking:
            return None
        booking.status="cancelled"
        await db.commit()
        await db.refresh(booking)
        return booking
    @staticmethod
    async def get_user_bookings(db:AsyncSession,user_id:int):
        result = await db.execute(select(Booking).where(Booking.user_id==user_id))
        return result.scalars().all()
    @staticmethod
    async def pay_booking(db:AsyncSession,booking_id:int):
        result = await db.execute(select(Booking).where(Booking.id==booking_id))
        booking = result.scalar_one_or_none()
        if not booking:
            return None
        booking.is_paid=True
        booking.status = "paid"
        await db.commit()
        await db.refresh(booking)
        return booking
