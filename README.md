# 온라인 서점을 위한 백엔드 서비스

### 실행 방법
1. python 설치 (사용한 버전: 3.13.3)
2. git 프로젝트 복제
   ```
   https://github.com/ohjisu/rgt_book_store.git
   ```
3. 이메일에 첨부되어있는 .env 파일을 프로젝트 루트 폴더에 다운로드 합니다
4. 터미널에서 python 가상 환경 생성합니다
   ```
   python -m venv .venv
   ```
5. 가상환경 활성화

   - for Windows
      ```
       .\.venv\Scripts\activate.ps1
       ```
   - for Ubuntu 18.04
      ```
      source .venv/bin/activate
       ```
6. 프로젝트 구동에 필요한 라이브러리를 다운로드 합니다
   ```
   pip install -r requirements.txt  
   ```
7. 프로젝트 실행 명령어
   ```
   uvicorn app.main:app --reload
   ```


### Hosting
- https://render.com/
- Render 사이트의 Static Sites, Web Services 서비스를 이용했습니다

### DB
- PostgreSQL
- Render Postgre 서비스를 이용했습니다

### Backend
- Python 3.13.3
- FastAPI 0.115.12


### Package
```
app/
├── crud/  # 데이터베이스에 대한 Create, Read, Update, Delete 작업 처리
├── db/ # 데이터베이스 연결, 테이블 생성 및 세션 관리
├── models/ # 테이블 구조를 정의하는 ORM Model
├── routes/ # API Endpoint 정의
├── schemas/ # 요청, 응답 데이터의 스키마를 정의
└── services/ # 비즈니스 로직. crud와 routes의 중간 계층
```

### API List
1. 책 목록 조회
    - [GET] /api/books
    - Query 값으로 page, page_size, title, author 4가지 값을 받을 수 있습니다
    - 기본값이 설정되어 있으므로 꼭 모든 Query 값을 보내지 않아도 괜찮습니다
   ```
    http://127.0.0.1:8000/api/books?page=1&page_size=10&title=흔한&author=백
    ```
2. 책 상세 정보 조회
    - [GET] /api/books/:id
    - 해당 아이디로 책이 조회되는 경우 id(아이디), title(제목), author(저자), sales(판매 수량) 값을 반환합니다
3. 책 추가
    - [POST] /api/books
    - JSON 데이터로 title(제목), author(저자) 값을 받습니다
    ```
    {
      "title":"미래를 팔다",
      "author":"옌스 베케르트"
    }
    ```
4. 책 정보 수정
    - [PUT] /api/books/:id
    - sales(판매수량), updated_at(업데이트 시간) 값을 변경합니다
5. 책 삭제
    - [DELETE] /api/books/:id
    - is_deleted, updated_at 값을 변경합니다
    - is_deleted 값에 따라 책 목록에 표시 유무가 결정됩니다
