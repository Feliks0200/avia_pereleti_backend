from pydantic import BaseModel
class UserCreate(BaseModel): # <-- создание пользователя
    email: str
    password: str
    full_name: str | None = None
    phone:str | None= None
    role:str="user" # <-- дефолт
class UserLogin(BaseModel): # <-- логин пользователя
    email: str
    password: str
class UserUpdate(BaseModel): # <-- обновление информации о пользователе
    email: str |None=None
    password: str |None=None
    full_name: str | None = None
    phone: str | None = None
