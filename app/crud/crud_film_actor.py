from sqlalchemy.orm import Session

from app.models.film_actor import FilmActor
from app.schemas.film_actor import FilmActorCreate, FilmActorInDB


class CRUDFilmActor:
    def create(self, db: Session, film_actor_create: FilmActorCreate) -> FilmActor:
        film_actor_in_db = FilmActorInDB(**film_actor_create.dict())
        film_actor_obj = FilmActor(**film_actor_in_db.dict())
        db.add(film_actor_obj)
        db.commit()


crud_film_actor = CRUDFilmActor()
