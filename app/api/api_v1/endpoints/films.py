from typing import List

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.film import FilmRead, FilmCreate, FilmUpdate
from app.crud.crud_film import crud_film

router = APIRouter()


@router.post("", response_model=FilmRead, response_model_by_alias=False)
def create_film(db: Session = Depends(get_db), *, film_create: FilmCreate):
    film = crud_film.create(db, film_create)
    return film


@router.get("", response_model=List[FilmRead], response_model_by_alias=False)
def read_films(db: Session = Depends(get_db)):
    films = crud_film.read_all(db)
    return films


@router.get("/{id}", response_model=FilmRead, response_model_by_alias=False)
def read_film(
    db: Session = Depends(get_db), id: int = Path(..., description="film id")
):
    film = crud_film.read_one(db, id)
    return film


# @router.put("/{id}", response_model=FilmRead, response_model_by_alias=False)
# def update_film(
    # db: Session = Depends(get_db),
    # id: int = Path(..., description="film id"),
    # *,
    # film_update: FilmUpdate
# ):
    # ...
# 
# 
# @router.delete("/{id}", response_model=FilmRead, response_model_by_alias=False)
# def delete_film(
    # db: Session = Depends(get_db), id: int = Path(..., description="film id")
# ):
    # film = crud_film.delete(db, id)
    # return film
