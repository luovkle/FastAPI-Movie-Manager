from typing import List

from sqlalchemy.orm import Session

from app.models.director import Director
from app.schemas.director import DirectorCreate, DirectorInDB
from app.core.exceptions import exceptions


class CRUDDirector:
    def get_by_name(self, db: Session, name: str) -> List[Director]:
        return db.query(Director).filter(Director.name == name).first()

    def create(self, db: Session, director_create: DirectorCreate) -> Director:
        if self.get_by_name(db, director_create.name):
            raise exceptions.NAME_NOT_AVAILABLE
        director_in_db = DirectorInDB(**director_create.dict())
        director_obj = Director(**director_in_db.dict())
        db.add(director_obj)
        db.commit()
        db.refresh(director_obj)
        return director_obj

    def delete(self):
        ...


crud_director = CRUDDirector()
