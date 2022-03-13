from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base_class import Base


class FilmActor(Base):
    __tablename__ = "film_actors"
    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)
    actor = relationship("Actor")
    actor_name = association_proxy("actor", attr="name")
