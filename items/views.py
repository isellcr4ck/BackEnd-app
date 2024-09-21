from fastapi import APIRouter
from .db import FAKE_ITEMS
from typing import Annotated

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("")
async def item_list(skip: int = 0, limit: int = 3):
    return FAKE_ITEMS[skip: skip + limit]
