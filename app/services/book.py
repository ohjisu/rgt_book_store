from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.book import (
    retrieve_book_list as book_crud_get_list,
    total_counts_book_list as book_crud_get_counts,
    create_book as book_crud_create,
    get_book as book_crud_get,
    update_book_sales as book_crud_update_sales,
    delete_book as book_crud_delete
)
from app.schemas.book import SearchBookListResponse, BookCreate


async def get_book_list(
        db: AsyncSession,
        page: int,
        page_size: int,
        title,
        author
):
    data = await book_crud_get_list(db=db, page=page, page_size=page_size, title=title, author=author)
    total_counts = await book_crud_get_counts(db=db, title=title, author=author)
    total_pages = (total_counts + page_size - 1) // page_size
    return SearchBookListResponse(
        data=data,
        page_size=page_size,
        page=page,
        total_counts=total_counts,
        total_pages=total_pages
    )


async def create_book(db: AsyncSession,book: BookCreate):
    await book_crud_create(db=db, book=book)


async def get_book(db: AsyncSession,book_id: int):
    return await book_crud_get(db=db, book_id=book_id)


async def update_book_sales(db: AsyncSession, book_id: int, sales: int):
    updated_book = await book_crud_update_sales(db, book_id, sales)
    if updated_book is None:
        raise ValueError("book not found")
    return updated_book



async def delete_book(db: AsyncSession, book_id: int):
    deleted_book = await book_crud_delete(db, book_id)
    if deleted_book is None:
        raise ValueError("book not found")
    return deleted_book