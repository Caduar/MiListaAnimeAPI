from typing import Optional
from pydantic import BaseModel

class Anime(BaseModel):
    id: Optional[str]
    name: str
    short_description: str
    genre: str
    stars: int