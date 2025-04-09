from typing import Union
from fastapi import FastAPI
from app.routes.books import router as book_router
from app.db.init_db import init_models
from app.db.session import engine

app = FastAPI()
app.include_router(book_router)


@app.on_event("startup")
async def on_startup_event():
    await init_models(engine)
