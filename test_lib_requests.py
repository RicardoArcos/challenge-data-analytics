import requests 
import os
import datetime

from decouple import config


dt = datetime.datetime.now()
date_one = dt.strftime("%Y-%B")
date_two = dt.strftime("%d-%m-%Y")

with requests.get(config('DATOS_MUSEOS')) as rq:
    os.makedirs(f'museos/{date_one}', exist_ok = True)
    with open(f'museos/{date_one}/museos-{date_two}.csv', 'wb') as file:
        file.write(rq.content)

with requests.get(config('DATOS_CINES')) as rq:
    os.makedirs(f'cines/{date_one}', exist_ok = True)
    with open(f'cines/{date_one}/cines-{date_two}.csv', 'wb') as file:
        file.write(rq.content)

with requests.get(config('DATOS_BIBLIOTECAS')) as rq:
    os.makedirs(f'bibliotecas/{date_one}', exist_ok = True)
    with open(f'bibliotecas/{date_one}/bibliotecas-{date_two}.csv', 'wb') as file:
        file.write(rq.content)