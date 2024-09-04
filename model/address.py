from sqlalchemy import Integer, asc,select
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db.db_setup import session
from .base import Base


class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(CHAR(100))
    mnemonic: Mapped[str] = mapped_column(CHAR(200))
    private_key: Mapped[str] = mapped_column(CHAR(100))

    def add_address(self, address, mnemonic, private_key):
        new_address = Address(address=address, mnemonic=mnemonic, private_key=private_key)
        session.add(new_address)
        session.commit()
        session.refresh(new_address)
        return new_address

    def get_list(self):
        smpt = select(Address.id, Address.address, Address.private_key).order_by(asc(Address.id)).limit(5)
        data = session.execute(smpt).mappings().all()
        session.close()
        return data
