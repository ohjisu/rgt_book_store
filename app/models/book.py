from sqlalchemy import Column, Integer, DateTime, String, Boolean, UniqueConstraint
from datetime import datetime
from app.models.base import Base


class Book(Base):
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    sales = Column(Integer, default=0, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    __table_args__ = (
        UniqueConstraint('title','author', name='uiq_title_author'),
    )