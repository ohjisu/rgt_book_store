from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.book import BookCreate, BookUpdate
from app.services.book import (
    get_book_list,
    create_book,
    get_book,
    update_book_sales,
    delete_book as book_service_delete
)

router = APIRouter(prefix="/api/books")


@router.get("", summary="책 목록 조회")
async def search_book_list(
    title: str = Query(None, description="제목"),
    author: str = Query(None, description="저자"),
    page: int = Query(1, ge=1, description="페이지 번호"),
    page_size: int = Query(10, ge=10, le=100, description="페이지 당 항목 수"),
    db: AsyncSession = Depends(get_db)
):
    """
    한 페이지당 10개 항목을 조회하는 페이지네이션 적용.

    제목, 저자로 필터링 검색.
    """
    res = await get_book_list(
        db=db,
        page=page,
        page_size=page_size,
        title=title,
        author=author
    )
    return res


@router.get("/{id}", summary="책 상세 정보 조회")
async def book_detail(
        id: int,
        db: AsyncSession = Depends(get_db)
):
    """
    아이디 값으로 책 상세 정보 조회.
    """
    return await get_book(db=db, book_id=id)


@router.post("", summary="책 추가")
async def save_book(
        request: BookCreate,
        db: AsyncSession = Depends(get_db)
):
    await create_book(db=db, book=request)
    return None


@router.put("/{id}", summary="책 정보 수정")
async def update_book(
        request: BookUpdate,
        id: int,
        db: AsyncSession = Depends(get_db)
):
    """
    판매 수량 조절 기능.
    """
    try:
        updated_book = await update_book_sales(db=db, book_id=id, sales=request.sales)
        return updated_book
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{id}", summary="책 삭제2222")
async def delete_book(
        id: int,
        db: AsyncSession = Depends(get_db)
):
    try:
        deleted_book = await book_service_delete(db=db, book_id=id)
        return deleted_book
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))