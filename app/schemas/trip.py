from pydantic import BaseModel


class TripCreate(BaseModel): # <-- создание билета
    from_city : str | None=None
    to_city : str | None=None
    price : float