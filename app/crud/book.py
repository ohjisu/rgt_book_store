from typing import List
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.book import Book
from app.schemas.book import BookCreate


async def create_book(db: AsyncSession, book: BookCreate):
    try:
        async with db.begin():
            db_book = Book(title=book.title, author=book.author)
            db.add(db_book)
    except SQLAlchemyError as e:
       await db.rollback()
    else:
       await db.commit()


async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id==book_id))
    return result.scalar_one_or_none()


async def update_book_sales(db: AsyncSession, book_id: int, sales: int):
    book = await get_book(db=db, book_id=book_id)
    if not book:
        return None
    book.sales = sales
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book


async def delete_book(db: AsyncSession, book_id: int):
    book = await get_book(db=db, book_id=book_id)
    if not book:
        return None
    book.is_deleted = True
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book



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
        query = query.where(Book.title.like(f"%{title}%"))
    if author:
        query = query.where(Book.author.like(f"%{author}%"))
    query = query.order_by(desc(Book.id)).limit(page_size).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


async def total_counts_book_list(
        db: AsyncSession,
        title: str,
        author: str
):
    query = select(func.count()).select_from(Book).where(Book.is_deleted.is_(False))
    if title:
        query = query.where(Book.title.like(f"%{title}%"))
    if author:
        query = query.where(Book.author.like(f"%{author}%"))

    result = await db.execute(query)
    return result.scalar()
