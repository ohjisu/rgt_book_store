from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from app.models.base import Base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql+asyncpg://")

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=20,
    echo=False,
    logging_name="RGT.LOGGER",
    connect_args={"ssl": True}
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    # expire_on_commit=False
)

Base: DeclarativeMeta = declarative_base(cls=Base)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session