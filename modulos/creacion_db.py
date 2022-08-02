from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine

from decouple import config

Base = declarative_base()
engine = create_engine(f"postgresql://{config('USER')}:{config('PASSWORD')}@{config('SERVER')}:{config('PORT')}/{config('DB_NAME')}")

