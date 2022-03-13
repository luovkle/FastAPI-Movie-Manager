from pydantic import BaseModel


class FilmActorBase(BaseModel):
    film_id: int
    actor_id: int


class FilmActorCreate(FilmActorBase):
    ...


class FilmActorInDB(FilmActorBase):
    ...
