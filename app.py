from fastapi import FastAPI
from routes.animes_route import anime

app = FastAPI(tittle = "Animes Vistos API",
              description = "Simple API to check which animes Mar and me watched or we're watching",
              version = "1.0.0",
              openapi_tags=[{
                  "name": "Animes",
                  "description": "animes routes"
              }])
app.include_router(anime)