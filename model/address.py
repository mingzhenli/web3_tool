from sqlalchemy import Integer, asc,select
from sqlalchemy.dialects.mysql import CHAR, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db.db_setup import session
from .base import Base


class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(VARCHAR(100))
    mnemonic: Mapped[str] = mapped_column(VARCHAR(200))
    private_key: Mapped[str] = mapped_column(VARCHAR(100))
    project: Mapped[str] = mapped_column(VARCHAR(100))

    def add_address(self, address, mnemonic, private_key, project):
        new_address = Address(address=address, mnemonic=mnemonic, private_key=private_key, project=project)
        session.add(new_address)
        session.commit()
        session.refresh(new_address)
        return new_address

    def get_list(self,project):
        smpt = select(Address.id, Address.address, Address.private_key).order_by(asc(Address.id)).filter_by(project = f'{project}').limit(54)
        data = session.execute(smpt).mappings().all()
        session.close()
        return data
