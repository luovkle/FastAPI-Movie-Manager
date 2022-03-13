from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    actors = relationship("FilmActor")
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)
    director = relationship("Director")
