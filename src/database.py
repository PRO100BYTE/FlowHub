from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import UsersDataBaseURL
from sqlalchemy.orm import DeclarativeBase

users_engine = create_async_engine(url=UsersDataBaseURL())

users_session = async_sessionmaker(bind=users_engine, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
