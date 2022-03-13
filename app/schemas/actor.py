from pydantic import BaseModel, Field


class ActorBase(BaseModel):
    name: str


class ActorCreate(ActorBase):
    ...


class ActorRead(ActorBase):
    id: int = Field(alias="actor_id")
    name: str = Field(alias="actor_name")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "string",
                "id": 0
            }
        }


class ActorUpdate(ActorBase):
    ...


class ActorInDB(ActorBase):
    ...
