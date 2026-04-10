from sqlalchemy import String, ForeignKey, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

class Base(DeclarativeBase): pass # <-- базовый класс

class User(Base): # <-- пользователи
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String,unique=True)
    password:Mapped[str]=mapped_column(String)
    full_name:Mapped[str]=mapped_column(String,nullable=True)
    phone:Mapped[str]=mapped_column(String,nullable=True)
    role:Mapped[str]=mapped_column(String,default="user")
class Trip(Base): # <-- билеты
    __tablename__ = 'trips'
    id:Mapped[int]=mapped_column(primary_key=True)
    from_city:Mapped[str]=mapped_column(String)
    to_city:Mapped[str]=mapped_column(String)
    price:Mapped[float]=mapped_column(Float)
class Booking(Base): # <-- бронирование
    __tablename__ = 'bookings'
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('users.id'))
    trip_id:Mapped[int]=mapped_column(ForeignKey('trips.id'))
    status:Mapped[str]=mapped_column(String,default="created")
    is_paid:Mapped[bool]=mapped_column(Boolean,default=False)