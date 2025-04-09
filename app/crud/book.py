from typing import List
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.book import Book
from app.schemas.book import BookCreate


async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def retrieve_book_list(
        db: AsyncSession,
        page: int,
        page_size: int,
        title: str,
        author: str,
):
    offset = (page-1) * page_size
    query = select(Book).where(Book.is_deleted.is_(False))
    if title:
        query = query.where(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.where(Book.author.ilike(f"%{author}%"))
    query = query.limit(page_size).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


async def total_counts_book_list(
        db: AsyncSession,
        title: str,
        author: str
):
    query = select(func.count()).select_from(Book).where(Book.is_deleted.is_(False))
    if title:
        query = query.where(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.where(Book.author.ilike(f"%{author}%"))

    result = await db.execute(query)
    return result.scalar()
