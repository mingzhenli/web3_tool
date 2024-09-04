from typing import Optional

from sqlalchemy import DECIMAL, Integer, TIMESTAMP, text, select
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import decimal

from db.db_setup import session


class Base(DeclarativeBase):
    pass


class Transactions(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(20, 11))
    hash: Mapped[str] = mapped_column(VARCHAR(255))
    status: Mapped[Optional[int]] = mapped_column(TINYINT, server_default=text("'0'"))
    update_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    process: Mapped[Optional[str]] = mapped_column(VARCHAR(255))


    #新增转帐记录
    def create(self,data):
        model = Transactions(address_id=data['address_id'],
                             amount=data['amount'],
                             hash=data['hash'],
                             process=data['process'],
                             status=data['status']
                             )
        session.add(model)
        session.commit()
        session.close()
        return model

    #修改交易状态
    def update_status(self, id, status):
        model = session.query(Transactions).filter(Transactions.id == id).first()
        model.status = status
        session.commit()
        session.close()
        return model

    #查询交易中间表
    def get_list(self, status = 0):
        build_sql = select(Transactions.id,Transactions.address_id,Transactions.hash).filter(Transactions.status == status)
        data = session.execute(build_sql).mappings().all()
        session.close()
        return data

