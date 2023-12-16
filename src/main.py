from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from users_orm import User


class UsersAddition(BaseModel):
    name: str
    nickName: str
    skills: list[str]
    tg: str
    email: str
    vk: str
    word: bool
    word_experience: str


app = FastAPI()


@app.post("/register")
async def register(user: UsersAddition):
    if User.check_users_exists(user.email):
        raise HTTPException(status_code=401, detail="user is already exist")
    await User.add_new_user(user)
    raise HTTPException(status_code=200, detail="user is successfully added")
