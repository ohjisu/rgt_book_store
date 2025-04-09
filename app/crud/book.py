from typing import List
from sqlalchemy import select, false
from sqlalchemy.ext.asyncio import AsyncSession


async def retrieve_book_list(
        db: AsyncSession
):
    result = await db.execute(
        select(Book)
        .where(Book.is_deleted.is_(false()))
    )
    return result.scalars().all()


async def total_counts_book_list(
        db: AsyncSession
):
    result = await db.execute(
        select(Book)
        .where(Book.is_deleted.is_(false()))
    )
    return result.count()
