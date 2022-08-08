CREATE TABLE IF NOT EXISTS primera_tabla (
    index bigint NOT NULL PRIMARY KEY,
    cod_localidad bigint,
    id_provincia bigint,
    id_departamento bigint,
    categoria varchar(255),
    provincia varchar(255),
    localidad varchar(255),
    nombre varchar(255),
    direccion varchar(255),
    cp varchar(50),
    num_telefono varchar(15),
    mail varchar(50),
    web varchar(50)
);

CREATE TABLE IF NOT EXISTS segunda_tabla (
    index bigint NOT NULL PRIMARY KEY,
    categoria varchar(50),
    fuente varchar(255),
    provincia varchar(255),
    registros_categoria bigint,
    registros_fuente bigint,
    registros_provincia_categoria bigint
);

CREATE TABLE IF NOT EXISTS tercera_tabla (
    index bigint NOT NULL PRIMARY KEY,
    provincia varchar(255),
    pantallas bigint,
    butacas bigint,
    espacio_INCAA varchar(255)
);
