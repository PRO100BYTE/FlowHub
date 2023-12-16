from database import users_engine, users_session
from models import UsersBase
from main import UsersAddition
from models import Users
from sqlalchemy import select


class User:
    @staticmethod
    async def create_all_tables():
        async with users_engine.begin() as conn:
            await conn.run_sync(UsersBase.metadata.create_all())

    @staticmethod
    async def add_new_user(user: UsersAddition):
        async with users_session() as session:
            skills = user.skills
            for skill in skills:
                user_obj = Users(name=user.name, nickName=user.nickName,
                                 skills=skill, telegram=user.tg, email=user.email, vk=user.vk,
                                 work=user.word, work_experience=user.word_experience)
                session.add(user_obj)
            session.commit()

    @staticmethod
    async def check_users_exists(email):
        async with users_session() as session:
            query = select(Users).filter_by(email=email)
            res = await session.execute(query)
            user = res.first()
            return user is not None
