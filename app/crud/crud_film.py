from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models.film import Film
from app.schemas.film import FilmCreate, FilmInDB
from app.schemas.director import DirectorCreate
from app.schemas.actor import ActorCreate
from app.schemas.film_actor import FilmActorCreate
from app.core.exceptions import exceptions
from app.crud.crud_director import crud_director
from app.crud.crud_actor import crud_actor
from app.crud.crud_film_actor import crud_film_actor


class CRUDFilm:
    def get_by_title(self, db: Session, title: str) -> Optional[Film]:
        return db.query(Film).filter(Film.title == title).first()

    def get_by_id(self, db: Session, id) -> Optional[Film]:
        return db.query(Film).filter(Film.id == id).first()

    def create(self, db: Session, film_create: FilmCreate) -> Film:
        if self.get_by_title(db, film_create.title):
            raise exceptions.TITLE_NOT_AVAILABLE
        director = crud_director.get_by_name(db, film_create.director.name)
        if not director:
            director_create = DirectorCreate(name=film_create.director.name)
            director = crud_director.create(db, director_create)
        actors = []
        for film_create_actor in film_create.actors:
            actor = crud_actor.get_by_name(db, film_create_actor.name)
            if not actor:
                actor_create = ActorCreate(name=film_create_actor.name)
                actor = crud_actor.create(db, actor_create)
            actors.append(actor)
        film_in_db = FilmInDB(**film_create.dict(), director_id=director.id)
        film_obj = Film(**film_in_db.dict())
        db.add(film_obj)
        db.commit()
        db.refresh(film_obj)
        for actor in actors:
            film_actor_create = FilmActorCreate(film_id=film_obj.id, actor_id=actor.id)
            crud_film_actor.create(db, film_actor_create)
        return film_obj

    def read_one(self, db: Session, id: int) -> Film:
        film = (
            db.query(Film)
            .options(joinedload(Film.actors))
            .filter(Film.id == id)
            .first()
        )
        if not film:
            raise exceptions.FILM_NOT_FOUND
        return film

    def read_all(self, db: Session) -> List[Film]:
        return db.query(Film).options(joinedload(Film.actors)).all()

    def update(self, db: Session, id: int) -> Film:
        ...

    # Drop film_actor rows
    def delete(self, db: Session, id: int) -> Film:
        film = self.get_by_id(db, id)
        if not film:
            raise exceptions.FILM_NOT_FOUND
        db.delete(film)
        db.commit()
        return film


crud_film = CRUDFilm()
