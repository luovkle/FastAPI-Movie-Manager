from pydantic import BaseModel


class DirectorBase(BaseModel):
    name: str


class DirectorCreate(DirectorBase):
    ...


class DirectorRead(DirectorBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class DirectorInDB(DirectorBase):
    ...
