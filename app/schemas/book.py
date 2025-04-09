from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime


class BookUpdate(BaseModel):
    sales: int


class BookSchema(BaseModel):
    id: int
    title: str
    author: str


class SearchBookListResponse(BaseModel):
    total_counts: int
    page_number: int
    page_size: int
    data: List[BookSchema]