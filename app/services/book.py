from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.book import (
    retrieve_book_list as book_crud_get_list,
    total_counts_book_list as book_crud_get_counts,
)
from app.schemas.book import SearchBookListResponse


async def get_book_list(
        db: AsyncSession,
        page: int,
        page_size: int
):
    data = await book_crud_get_list(db=db)
    total_counts = await book_crud_get_counts(db=db)
    return SearchBookListResponse(
        data=data,
        page_size=page_size,
        page=page,
        total_counts=total_counts
    )
