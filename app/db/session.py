from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from app.models.base import Base

engine = create_async_engine(
    "db_urls",
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=20,
    echo=False,
    logging_name="RGT.LOGGER"
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

Base: DeclarativeMeta = declarative_base(cls=Base)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session