from pydantic import BaseModel


class BookingCreate(BaseModel): # <-- создания брони (кстати недоделанный :3)
    user_id : int
    trip_id : int