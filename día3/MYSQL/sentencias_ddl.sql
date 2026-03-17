CREATE DATABASE db_matriculas
    DEFAULT CHARACTER SET = 'utf8mb4';

show databases;
use db_matriculas;
show tables;

-- SENTENCIAS DDL
-- CREAR UNA TABLA
CREATE TABLE alumno(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

-- MODIFICAR UNA TABLA
ALTER TABLE alumno
ADD COLUMN nota INT default 0;

-- ELIMINAR TABLA
DROP TABLE alumno;