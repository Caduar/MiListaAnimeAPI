from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

animes = Table("animes", meta, Column(
    "id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("short_description", String(255)),
    Column("genre", String(255)),
    Column("stars", Integer))

meta.create_all(engine)