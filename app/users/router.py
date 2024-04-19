from fastapi import APIRouter

from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(user_data.email)