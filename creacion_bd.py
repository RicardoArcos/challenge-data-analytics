from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text

from decouple import config

from config import *

def get_engine():
    ''' Se crea la conexión a la base de datos a partir del usuario, contraseña, host, puerto y nombre
    proporcinados por el usuario. Retorna un elemento de conexión.'''
    url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine

engine = get_engine()

def create_tables():
    ''' Esta función crea las tablas de la base de datos en base a los scripts sql. '''
    with engine.connect() as con:
        with open("scripts_sql/tablas.sql") as file:
            consulta = text(file.read())
            con.execute(consulta)
            
def add_columns():
    ''' Se añaden las columnas extras a las tablas de la base de datos. '''
    with engine.connect() as con:
        with open("scripts_sql/nueva_columna.sql") as file:
            consulta = text(file.read())
            con.execute(consulta)
