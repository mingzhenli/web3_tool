from typing import Optional

from sqlalchemy import Integer, String, text,select
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db.db_setup import session

class Base(DeclarativeBase):
    pass

class SendAddress(Base):
    __tablename__ = 'send_address'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_general_ci'))
    status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    hash: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_general_ci'))
    project: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_general_ci'))
    balance:Mapped[int] = mapped_column(Integer)

    def get_send_list(self,start_id,end_id):
        smpt =  (select(SendAddress.id, SendAddress.address, SendAddress.status).filter(SendAddress.status == 0).
                 filter(SendAddress.id.between(start_id,end_id))
                 )
        list  = session.execute(smpt).mappings().all()
        session.close()
        return list

    def update(self, id, data):
        res = session.query(SendAddress).filter(SendAddress.id == id).update(data)
        session.commit()
        session.close()
        return res


    def get_balance_list(self):
        smpt =  (select(SendAddress.id, SendAddress.address, SendAddress.status).filter(SendAddress.balance.is_(None))
                 )
        list  = session.execute(smpt).mappings().all()
        session.close()
        return list

