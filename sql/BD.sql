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


CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) CHECK (precio > 0),
    cantidad INT DEFAULT 0 CHECK (cantidad >= 0)
);


INSERT INTO productos (nombre, precio)
VALUES ('Producto A', 19.99),
    ('Producto B', 29.99);


UPDATE productos
SET cantidad = 100
WHERE precio > 20;


DELETE FROM usuarios
WHERE id NOT IN (
    SELECT MIN(id)
    FROM usuarios
    GROUP BY correo
);


SELECT nombre
FROM productos
WHERE precio > (
    SELECT AVG(precio)
    FROM productos
);

SELECT * 
FROM productos
ORDER BY precio DESC
LIMIT 3;

DELIMITER //

CREATE TRIGGER antes_insertar_producto
BEFORE INSERT ON productos
FOR EACH ROW
BEGIN
    IF NEW.precio < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio no puede ser negativo';
    END IF;
END //

DELIMITER ;


SELECT usuarios.nombre, pedidos.monto
FROM usuarios
LEFT JOIN pedidos ON usuarios.id = pedidos.usuario_id;

CREATE TEMPORARY TABLE productos_temporales (
    id INT,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2)
);

INSERT INTO productos_temporales (id, nombre, precio)
VALUES (1, 'Producto Temporal', 15.99);

SELECT * FROM productos_temporales;


CREATE TABLE detalle_pedidos (
    pedido_id INT,
    producto_id INT,
    cantidad INT,
    PRIMARY KEY (pedido_id, producto_id)
);


SELECT * 
FROM productos
WHERE nombre LIKE '%Producto%';


SELECT NOW() AS fecha_actual,
       DATE_ADD(NOW(), INTERVAL 7 DAY) AS fecha_siguiente,
       DATE_FORMAT(NOW(), '%d-%m-%Y') AS fecha_formateada;


RENAME TABLE productos TO productos_inventario;

DROP TABLE IF EXISTS productos_temporales;

SELECT * 
FROM usuarios
INTO OUTFILE '/var/lib/mysql-files/usuarios.csv'
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';


LOAD DATA INFILE '/var/lib/mysql-files/usuarios.csv'
INTO TABLE usuarios
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';


LOAD DATA INFILE '/var/lib/mysql-files/usuarios.csv'
INTO TABLE usuarios
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';


SELECT MAX(precio) AS segundo_mayor
FROM productos
WHERE precio < (
    SELECT MAX(precio)
    FROM productos
);


CREATE INDEX idx_precio
ON productos(precio);


OPTIMIZE TABLE usuarios;


SELECT * 
FROM productos PARTITION (p0, p1);


CREATE TABLE ventas (
    id INT NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(10, 2),
    PRIMARY KEY (id, fecha)
)
PARTITION BY RANGE (YEAR(fecha)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);


SELECT COUNT(DISTINCT correo) AS correos_unicos
FROM usuarios;


SELECT * 
FROM usuarios
WHERE correo REGEXP '^[a-zA-Z0-9._%+-]+@gmail\\.com$';


CREATE TABLE usuarios_copia AS
SELECT * 
FROM usuarios;

SELECT * 
FROM productos
ORDER BY precio DESC
LIMIT 3, 5;
