from typing import Optional

from sqlalchemy.orm import Session

from app.models.actor import Actor
from app.schemas.actor import ActorCreate, ActorInDB
from app.core.exceptions import exceptions


class CRUDActor:
    def get_by_name(self, db: Session, name: str) -> Optional[Actor]:
        return db.query(Actor).filter(Actor.name == name).first()

    def create(self, db: Session, actor_create: ActorCreate) -> Actor:
        if self.get_by_name(db, actor_create.name):
            raise exceptions.NAME_NOT_AVAILABLE
        actor_in_db = ActorInDB(**actor_create.dict())
        actor_obj = Actor(**actor_in_db.dict())
        db.add(actor_obj)
        db.commit()
        db.refresh(actor_obj)
        return actor_obj


crud_actor = CRUDActor()
