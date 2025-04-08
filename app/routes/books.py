from fastapi import APIRouter, Depends, Query

router = APIRouter(prefix="/api/books")


@router.get("",
            summary="책 목록 조회")
def search_book_list(
    title: str = Query(None, description="제목"),
    author: str = Query(None, description="저자"),
    page: int = Query(1, ge=1, description="페이지 번호"),
    page_size: int = Query(10, ge=10, le=100, description="페이지 당 항목 수")
):
    """
    한 페이지당 10개 항목을 조회하는 페이지네이션 적용.

    제목, 저자로 필터링 검색.
    """
    print(title, author, page, page_size)
    return []


@router.get("/{id}",
            summary="책 상세 정보 조회")
def book_detail(id: int):
    return {"book": {
        "id": id
    }}


@router.post("",
             summary="책 추가")
def save_book():
    return None


@router.put("/{id}",
            summary="책 정보 수정")
def update_book(id: int):
    """
    판매 수량 조절 기능.
    """
    return id


@router.delete("/{id}",
               summary="책 삭제")
def delete_book(id: int):
    return id