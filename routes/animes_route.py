from fastapi import APIRouter, Response, status
from config.db import conn
from models.anime_models import animes
from schemas.animes_schema import Anime
from starlette.status import HTTP_204_NO_CONTENT

anime = APIRouter()


@anime.get("/animes", response_model=list[Anime], tags=["Animes"])
def get_animes():
    return conn.execute(animes.select()).fetchall()


@anime.post("/animes", response_model=Anime, tags=["Animes"])
def create_animes(anime: Anime):
    new_anime = {"name": anime.name,
                 "short_description": anime.short_description,
                 "genre": anime.genre,
                 "stars": anime.stars}
    result = conn.execute(animes.insert().values(new_anime))
    return conn.execute(animes.select().where(animes.c.id == result.lastrowid)).first()


@anime.get("/animes/{id}", response_model=Anime, tags=["Animes"])
def get_anime(id: str):
    result = conn.execute(animes.select().where(animes.c.id == id)).first()
    return result


@anime.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Animes"])
def delete_anime(id: str):
    result = conn.execute(animes.delete().where(animes.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@anime.put("/animes/{id}", response_model=Anime, tags=["Animes"])
def update_user(id: str, anime: Anime):
    conn.execute(animes.update().values(name=anime.name,
                                        short_description=anime.short_description,
                                        genre=anime.genre, stars=anime.stars).where(animes.c.id == id))
    return conn.execute(animes.select().where(animes.c.id == id)).first()
