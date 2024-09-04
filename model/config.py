from typing import Optional

from sqlalchemy import Integer, JSON
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .base import Base
from db.db_setup import session
class Config(Base):
    __tablename__ = 'config'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    key: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    value: Mapped[Optional[dict]] = mapped_column(JSON)
    project: Mapped[Optional[str]] = mapped_column(VARCHAR(255))

    def get_value_by_key(self, id, key=None):
        query = session.query(Config)
        if id :
            query = query.filter(Config.id == id)
        elif key :
            query = query.filter(Config.key == key)
        data =query.first()
        session.close()
        return data
