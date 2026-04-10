from fastapi import FastAPI

from app.models.models import Base # <-- база данных
from app.routers.admin import admin_router # <-- админ роутер
from app.routers.auth import router # <-- роутер для аутинификации
from app.routers.bookings import book_router # <-- бронирование роутер
from app.routers.trips import trips_router # <-- билеты роутер
from app.routers.users import user_router # <-- пользователи роутер
from database import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(router)
app.include_router(book_router)
app.include_router(trips_router)
app.include_router(user_router)
app.include_router(admin_router)