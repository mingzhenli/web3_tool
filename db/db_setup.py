# db_setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base

DATABASE_URI = 'mysql+pymysql://web3_tool:123989@192.168.2.88:3306/web3_tool'  # 或者使用其他数据库 URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
