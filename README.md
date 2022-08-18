# Challenge Data Analytics - Python 🚀

En este challenge de Alkemy consiste en extraer tres conjuntos de datos, procesarlos usando Pandas y despues guardarlos en una base de datos.

## Instalación del proyecto

Para instalar el proyecto es necesario clonarlo desde el repositorio de github, para clonar el repositorio se debe usar el siguiente comando:

`git clone https://github.com/RicardoArcos/challenge-data-analytics`

Después de haber clonado el repositorio es necesario instalar las librerias necesarias, para hacerlo podemos usarlo el siguiente comando:

`pip install -r requirements.txt`

Para que el proyecto funcione bien es necesario crear las variables de entorno para que la conexión con la base de datos se exitosa, es por eso que por lo que se debe de crear un archivo *.env * en la raiz de la carpeta del proyecto. Se deben definir las siguientes variables de entorno:

| Variable | Descripción                    |
| ------------- | ------------------------------ |
| `DATOS_MUSEOS = ''`      | Enlace para la obtención de los datos de los museos.  |
| `DATOS_CINES = ''`      | Enlace para la obtención de los datos de los cines.      |
| `DATOS_BIBLIOTECA = ''`      | Enlace para la obtención de los datos de las bibliotecas.      |
| `USER = `      | Usuario de la base de datos.    |
| `PASSWORD = `      | Contraseña de la base de datos.    |
| `SERVER = `      | Servidor de la base de datos.    |
| `PORT = `      | Puerto de la base de datos.    |
| `DB_NAME = `      | Nombre de la base de datos.    |

