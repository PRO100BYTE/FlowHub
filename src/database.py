from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import UsersDataBaseURL, AdminDataBaseURL

users_engine = create_async_engine(UsersDataBaseURL())
admin_engine = create_async_engine(AdminDataBaseURL())

users_session = async_sessionmaker(users_engine)
admin_session = async_sessionmaker(admin_engine)
