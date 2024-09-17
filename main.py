from fastapi import FastAPI
from users.views import router as users_router

app = FastAPI(title="My first API")
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "start project"}

