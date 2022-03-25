# How to use

## Get code

```sh
git clone https://github.com/luovkle/FastAPI-Movie-Manager.git
cd FastAPI-Movie-Manager
```

## Run postgres

Example with docker.

```sh
docker run --rm -d -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=app postgres:13.3-alpine
```

Custom values can be used in environment variables, but must be specified in app/core/config.py.

## Install dependencies in a virtual environment

Example with pipenv.

```sh
pipenv install && pipenv shell
```

Example with pip and venv.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Create the tables in the database

```sh
alembic upgrade head
```

## Running the server

```sh
uvicorn app.main:app
```
