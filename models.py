from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class Item(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)

