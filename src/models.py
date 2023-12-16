from sqlalchemy import MetaData, Index
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base
from database import users_engine, admin_engine
import enum

users_meta_data = MetaData(users_engine)
admins_meta_data = MetaData(admin_engine)

UsersBase = declarative_base(metadata=users_meta_data)
AdminsBase = declarative_base(metadata=admins_meta_data)


class WorkExperience(enum.Enum):
    without_experience = "without_experience"
    year = "year"
    three_years = "three years"
    more_five_years = "more five years"


class Users(UsersBase):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    nickName: Mapped[str] = mapped_column()
    skills: Mapped[str] = mapped_column()
    telegram: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    vk: Mapped[str] = mapped_column()
    work: Mapped[bool] = mapped_column()
    work_experience: Mapped[WorkExperience]


class Admins(AdminsBase):
    __tablename__ = "admins"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()


index_email = Index("idx_check_login", Admins.login)
index_authorization = Index("idx_authorization", Admins.login, Admins.password)
