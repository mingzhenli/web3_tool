from typing import Optional
from sqlalchemy import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import  Mapped, mapped_column
from db.db_setup import session
from .base import Base


class Btc(Base):
    __tablename__ = 'btc'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    web_name: Mapped[Optional[str]] = mapped_column(String(255))
    canuse: Mapped[Optional[int]] = mapped_column(TINYINT)