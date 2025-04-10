from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.books import router as book_router
from app.db.init_db import init_models
from app.db.session import engine

app = FastAPI()
app.include_router(book_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup_event():
    await init_models(engine)
