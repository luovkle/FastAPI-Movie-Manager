from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
