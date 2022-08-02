import requests
import os
import datetime
import pandas as pd

from decouple import config

#Variables fecha
dt = datetime.datetime.now()
date_one = dt.strftime("%Y-%B")
date_two = dt.strftime("%d-%m-%Y")

#Obteniendo los datos
with requests.get(config('DATOS_MUSEOS')) as rq:
    os.makedirs(f'museos/{date_one}', exist_ok=True)
    with open(f'museos/{date_one}/museos-{date_two}.csv', 'wb') as file:
        file.write(rq.content)

with requests.get(config('DATOS_CINES')) as rq:
    os.makedirs(f'cines/{date_one}', exist_ok=True)
    with open(f'cines/{date_one}/cines-{date_two}.csv', 'wb') as file:
        file.write(rq.content)

with requests.get(config('DATOS_BIBLIOTECAS')) as rq:
    os.makedirs(f'bibliotecas/{date_one}', exist_ok=True)
    with open(f'bibliotecas/{date_one}/bibliotecas-{date_two}.csv', 'wb') as file:
        file.write(rq.content)

#Manipulando los datos
df_museos = pd.read_csv(f'museos/{date_one}/museos-{date_two}.csv').set_axis(['cod_localidad', 
	'id_provincia', 'id_departamento', 'observaciones', 'categoria', 'subcategoria', 
	'provincia', 'localidad', 'nombre', 'domicilio', 'piso', 'cp', 'cod_area', 
	'num_telefono', 'mail', 'web', 'latitud', 'longitud', 'tipo_latlong', 
	'info_adicional', 'fuente', 'jurisdiccion', 'anio_inauguracion', 'anio_actualizacion'], 
	axis='columns')

df_cines = pd.read_csv(f'cines/{date_one}/cines-{date_two}.csv').set_axis(['cod_localidad','id_provincia','id_departamento',
    'observaciones','categoria','provincia','departamento',
    'localidad','nombre','direccion',
    'piso','cp','cod_area','num_telefono','mail','web',
    'info_adicional','latitud','longitud','tipo_latlong',
    'fuente','tipo_gestion','pantallas','butacas','espacio_INCAA','anio_actualizacion'],
    axis='columns')

df_bibliotecas = pd.read_csv(f'bibliotecas/{date_one}/bibliotecas-{date_two}.csv').set_axis(['cod_localidad','id_provincia',
    'id_departamento',
    'observaciones','categoria','subcategoria',
    'provincia','departamento',
    'localidad','nombre','direccion',
    'piso','cp','cod_area','num_telefono','mail','web',
    'info_adicional','latitud','longitud','tipo_latlong',
    'fuente','tipo_gestion','anio_inicio','anio_actualizacion'],
    axis='columns')

df_bd = pd.concat([df_museos,df_cines,df_bibliotecas])

#Creando la primera tabla
primera_tabla = df_bd.filter(['cod_localidad','id_provincia','id_departamento','categoria','provincia','localidad','nombre','direccion','cp','num_telefono','mail','web'])

#Creando la segunda tabla
values_categoria = df_bd.groupby(['categoria']).size().to_frame(name = 'registros_categoria')
values_fuente = df_bd.loc[:, ['fuente', 'categoria']].value_counts().to_frame(name = 'registros_fuente')
values_provincia = df_bd.loc[:, ['categoria', 'provincia']].value_counts().to_frame(name = 'registros_provincia_categoria')

segunda_tabla = values_categoria.merge(values_fuente, how='outer', left_index=True, right_index=True)
segunda_tabla = segunda_tabla.merge(values_provincia, how='outer', left_index=True, right_index=True)

#Creando la tercera tabla
tercera_tabla = df_cines.filter(['provincia','pantallas','butacas','espacio_INCAA'])
tercera_tabla.espacio_INCAA = tercera_tabla.espacio_INCAA.fillna(value=0)
tercera_tabla.espacio_INCAA = tercera_tabla.espacio_INCAA.replace(to_replace=['si','SI'], value=1)
