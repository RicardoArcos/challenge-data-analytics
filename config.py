from decouple import config

MUSEOS_URL = config('DATOS_MUSEOS')
CINES_URL = config('DATOS_CINES')
BIBLIOTECAS_URL = config('DATOS_BIBLIOTECAS')

USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('SERVER')
PORT = config('PORT')
DB_NAME = config('DB_NAME')
