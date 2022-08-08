from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text

from decouple import config

from config import *

def get_engine():
    url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine

engine = get_engine()

def create_tables():
    with engine.connect() as con:
        with open("scripts_sql/tablas.sql") as file:
            consulta = text(file.read())
            con.execute(consulta)
