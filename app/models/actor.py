from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
