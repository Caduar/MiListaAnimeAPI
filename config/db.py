from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:toor@localhost:3306/animedb")

meta = MetaData()

conn = engine.connect()