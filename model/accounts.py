from typing import Optional

from sqlalchemy import Float, Integer, text
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from db.db_setup import session
from .base import Base


class Accounts(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(VARCHAR(255))
    private_key: Mapped[str] = mapped_column(VARCHAR(255))
    base_status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    fraxtal_status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    mantal_status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    no_use: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    balance_base: Mapped[Optional[float]] = mapped_column(Float, server_default=text("'0'"))
    balance_fraxtal: Mapped[Optional[float]] = mapped_column(Float, server_default=text("'0'"))
    balance_mantal: Mapped[Optional[float]] = mapped_column(Float, server_default=text("'0'"))



    def get_user_info(self, id):
        data = session.query(Accounts).filter(Accounts.id == id).first()
        session.close()
        return data

    def get_user(self, id):
        data = session.query(Accounts).filter(Accounts.id < id).all()
        session.close()
        return data


