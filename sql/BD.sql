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


DELETE FROM usuarios
WHERE edad < 30;

ALTER TABLE usuarios
ADD COLUMN telefono VARCHAR(15);

ALTER TABLE usuarios
DROP COLUMN telefono;

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha DATE,
    monto DECIMAL(10, 2),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO pedidos (usuario_id, fecha, monto)
VALUES (1, '2025-01-13', 150.75),
       (2, '2025-01-12', 200.00);


SELECT usuarios.nombre, pedidos.fecha, pedidos.monto
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;

SELECT AVG(edad) AS promedio_edad, COUNT(*) AS total_usuarios
FROM usuarios;

SELECT edad, COUNT(*) AS cantidad
FROM usuarios
GROUP BY edad;

CREATE INDEX idx_nombre
ON usuarios(nombre);


DELIMITER //

CREATE PROCEDURE ObtenerUsuarios()
BEGIN
    SELECT * FROM usuarios;
END //

DELIMITER ;

CALL ObtenerUsuarios();


DELIMITER //

CREATE FUNCTION SumarNumeros(a INT, b INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN a + b;
END //

DELIMITER ;

CREATE VIEW vista_usuarios_pedidos AS
SELECT usuarios.nombre, pedidos.fecha, pedidos.monto
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;

START TRANSACTION;

UPDATE usuarios
SET edad = 35
WHERE id = 1;

DELETE FROM pedidos
WHERE id = 2;

COMMIT; -- Confirma los cambios
-- ROLLBACK; -- Revierte los cambios si es necesario
