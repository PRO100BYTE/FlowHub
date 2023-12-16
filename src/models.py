from sqlalchemy import MetaData, Index
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, users_engine

#users_meta_data = MetaData()


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    nickName: Mapped[str] = mapped_column()
    skills: Mapped[str] = mapped_column()
    telegram: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    vk: Mapped[str] = mapped_column()
    work: Mapped[bool] = mapped_column()
    work_experience: Mapped[str] = mapped_column()


index_skill = Index("idx_find_skill", Users.skills)
