from .database import Base
from sqlalchemy import Integer, Column


# 所有表的基类
class HasidMdl(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
