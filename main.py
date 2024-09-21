from fastapi import FastAPI
from users.views import router as users_router
from items.views import router as items_router

app = FastAPI(title="My first API")
app.include_router(users_router)
app.include_router(items_router)


@app.get("/")
async def root():
    return {"message": "start project"}

