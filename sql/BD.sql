CREATE DATABASE mi_base_de_datos;
USE mi_base_de_datos;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    edad INT
);
