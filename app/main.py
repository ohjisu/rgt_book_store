from typing import Union
from fastapi import FastAPI
from app.routes.books import router as book_router

app = FastAPI()
app.include_router(book_router)
