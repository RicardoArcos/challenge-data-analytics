from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from decouple import config

from config import *

def get_engine():
    url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine
