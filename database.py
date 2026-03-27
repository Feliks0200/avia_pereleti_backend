from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL="postgresql+asyncpg://postgres:Admin@localhost:5432/backendavia"
engine = create_async_engine(DATABASE_URL,echo=True)
sessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with sessionLocal() as session:
        yield session

# from datetime import datetime
#
# import sqlalchemy
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
# from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
#
# engine = create_async_engine('postgresql+asyncpg://postgres:Admin@localhost:5432/sqlAlchemyTest', echo=False)
# SessionMaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
#
#
# class Base(DeclarativeBase): pass
#
#
# class Users(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, index=True)
#     login = Column(String)
#     password = Column(String)
#     email = Column(String)
#     role = Column(String)
#
#     orders = relationship("Orders", back_populates="user")
#     races = relationship("Races", back_populates="user")
#
# class Races(Base):
#     __tablename__ = 'races'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     user_id = Column(Integer, ForeignKey('user.id'))
#
#     orders = relationship("Orders", back_populates="race")
#     user = relationship("Users",back_populates='races')
#
# class Order(Base):
#     __tablename__ = 'order'
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     raceid = Column(Integer, ForeignKey('races.id'))
#
#     user = relationship("Users",back_populates='orders')
#     race = relationship("Races",back_populates='orders')
