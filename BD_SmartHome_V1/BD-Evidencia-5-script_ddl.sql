-- Creacion de tablas
CREATE TABLE usuarios (
    id_usuario int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    password varchar(100) NOT NULL,
    es_admin boolean NOT NULL DEFAULT FALSE
);

CREATE TABLE dispositivos(
    id_dispositivo int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL UNIQUE,
    estado tinyint(1) NOT NULL DEFAULT 0,
    es_esencial boolean NOT NULL DEFAULT FALSE
);

CREATE TABLE automatizaciones ( 
    id_automatizacion INT AUTO_INCREMENT PRIMARY KEY, 
    nombre varchar(50) NOT NULL, 
    tipo varchar(50) NOT NULL 
);

CREATE TABLE automatizacion_dispositivo (
    id_automatizacion INT,
    id_dispositivo INT,
    PRIMARY KEY (id_automatizacion, id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id_dispositivo)
);