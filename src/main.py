import asyncio
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from users_orm import User
import uvicorn


class UsersAddition(BaseModel):
    name: str
    nickName: str
    skills: list[str]
    tg: str
    email: str
    vk: str
    work: bool
    work_experience: str


class NewsletterInfo(BaseModel):
    message: str
    skills: list[str]
    work: bool
    work_experience: str


async def create_database():
    await User.create_all_tables()


def fast_api_app():
    app = FastAPI(title="FastApi")

    @app.post("/register")
    async def register(user: UsersAddition):
        if await User.check_users_exists(user.email):
            raise HTTPException(status_code=401, detail="user is already exist")
        await User.add_new_user(user.name, user.nickName, user.skills, user.tg, user.email, user.vk, user.work,
                                user.work_experience)
        raise HTTPException(status_code=200, detail="user is successfully added")

    @app.post("/newsletter")
    async def newsletter_sender(newsletter: NewsletterInfo):
        users_social_media = await User.get_users_id_for_newsletter(newsletter.skills)
        print(users_social_media)
        # do newsletter
        raise HTTPException(status_code=201, detail="message is successfully send")

    return app


app = fast_api_app()

if __name__ == "__main__":
    asyncio.run(create_database())
    uvicorn.run(
        app="src.main:app",
        host="localhost",
        port=6100,
        reload=True
    )
