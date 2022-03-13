from typing import List

from pydantic import BaseModel

from app.schemas.actor import ActorRead, ActorCreate
from app.schemas.director import DirectorRead, DirectorCreate


class FilmBase(BaseModel):
    title: str


class FilmCreate(FilmBase):
    actors: List[ActorCreate]
    director: DirectorCreate


class FilmRead(FilmBase):
    id: int
    actors: List[ActorRead]
    director: DirectorRead

    class Config:
        orm_mode = True


class FilmUpdate(FilmBase):
    actors: List[ActorCreate]
    director: DirectorCreate


class FilmInDB(FilmBase):
    director_id: int
