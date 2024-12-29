CREATE DATABASE mi_base_de_datos;
USE mi_base_de_datos;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    edad INT
);

INSERT INTO usuarios (nombre, correo, edad)
VALUES ('Juan Pérez', 'juan@example.com', 30),
       ('Ana Gómez', 'ana@example.com', 25);


SELECT * FROM usuarios;

SELECT * FROM usuarios WHERE edad > 25;

UPDATE usuarios
SET edad = 31
WHERE nombre = 'Juan Pérez';
