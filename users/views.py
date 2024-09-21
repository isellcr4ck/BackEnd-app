from fastapi import APIRouter
from .db import FAKE_USERS
from .schemas import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
async def read_users(skip: int = 0, limit: int = 3):
    return FAKE_USERS[skip: skip + limit]


@router.post("/register")
async def insert_user_in_db(register: list[User]):
    FAKE_USERS.extend(register)
    return {"status": 200, "data": FAKE_USERS}


@router.get("/{user_id}/detail")
async def read_user_by_id(user_id: int):
    return [user for user in FAKE_USERS if user.get("id") == user_id]


@router.get("/{user_id}/name")
def get_user_name_by_id(user_id: int):
    current_user = list([user for user in FAKE_USERS if user.get("id") == user_id])[0]
    return {
        "id": current_user["id"],
        "name": current_user["name"],
    }


@router.post("/{user_id}")
def change_username(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, FAKE_USERS))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

