from sqlalchemy import create_engine

from decouple import config

engine = create_engine(f"postgresql://{config('USER')}:{config('PASSWORD')}@{config('SERVER')}:{config('PORT')}/{config('DB_NAME')}")

