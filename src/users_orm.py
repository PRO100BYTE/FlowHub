from database import users_engine, users_session, Base
from models import Users
from sqlalchemy import select


class User:
    @staticmethod
    async def create_all_tables():
        async with users_engine.begin() as conn:
            #await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def add_new_user(name, nickName, skills, tg, email, vk, work, word_experience):
        async with users_session() as session:
            for skill in skills:
                user_obj = Users(name=name, nickName=nickName,
                                 skills=skill, telegram=tg, email=email, vk=vk,
                                 work=work, work_experience=word_experience)
                session.add(user_obj)
            await session.commit()

    @staticmethod
    async def check_users_exists(email):
        async with users_session() as session:
            query = select(Users).filter_by(email=email)
            res = await session.execute(query)
            user = res.first()
            return user is not None

    @staticmethod
    async def get_users_id_for_newsletter(skills: list):
        users_telegram = set()
        async with users_session() as session:
            for skill in skills:
                query = select(Users).filter_by(skills=skill)
                res = await session.execute(query)
                result = res.scalars().all()
                print(res)
                for user in result:
                    users_telegram.add(user.telegram)
        return users_telegram
