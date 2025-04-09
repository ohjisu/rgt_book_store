from sqlalcmeny import Column, Integer, Datetime, String, Boolean
from datetime import datetime
from app.models.base import Base


class Book(Base):
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    sales = Column(Integer, default=0, nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
