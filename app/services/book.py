from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.book import (
    retrieve_book_list as book_crud_get_list,
    total_counts_book_list as book_crud_get_counts,
    create_book as book_crud_create,
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
    return SearchBookListResponse(
        data=data,
        page_size=page_size,
        page=page,
        total_counts=total_counts
    )


async def create_book(
        db: AsyncSession,
        book: BookCreate
):
    await book_crud_create(db=db, book=book)
