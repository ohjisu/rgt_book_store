from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str


class BookUpdate(BaseModel):
    sales: int


class BookSchema(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        from_attributes = True


class SearchBookListResponse(BaseModel):
    total_counts: int
    page: int
    page_size: int
    data: List[BookSchema]
