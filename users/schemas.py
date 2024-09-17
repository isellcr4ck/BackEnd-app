from pydantic import BaseModel
from typing import Optional
from .db import FAKE_USERS


class User1(BaseModel):
    id: int
    fullname: str = "Samuel"
    age: Optional[int] = None
    job: str = "without"
    friend_list: list[int] = []

    def __str__(self):
        return (f"{self.__class__.__name__}(id = {self.id}, fullname = {self.fullname}, "
                f"age = {self.age}, job = {self.job})")

    def add_friend(self, user_id: int):
        if user_id == self.id:
            raise ValueError("You can't invite yourself")
        return self.friend_list.append(user_id)

    @property
    def friends(self):
        print(self.friend_list)




Sam = User1(
    id=1,
    fullname="Samuel",
    age=28,
    job="cookMaster"
)

John = User1(
    id=2,
    fullname="John",
    job="developer"
)

Paul = User1(
    id=3,
    fullname="Paul",
    age=35,
)

count = 0
for i in range(0, len(FAKE_USERS)):
    count+=1

class User(BaseModel):
    id: int = len(FAKE_USERS) + 1
    username: str = "TestUN"
    name: str = "Con"
    age: Optional[int] = None
    job: Optional[str] = None