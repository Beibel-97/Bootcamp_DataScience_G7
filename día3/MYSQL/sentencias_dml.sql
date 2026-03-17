use db_matriculas;
-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

-- INSERT
insert into alumno(nro_documento,nombre) values('1000','oscar');

INSERT INTO alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

-- SELECT READ O LEER DATOS
select * from alumno;
select nombre,nota from alumno;
-- select con where
select nombre,nota from alumno
where nota > 10;
select nombre,nota from alumno
where nombre like '%l%';

-- ACTUALIZAR Y ELIMINAR DATOS
UPDATE alumno set email = 'codigo@gmail.com';
-- ACTUALIZAR CON CONDICIONAL WHERE
UPDATE alumno set email = 'cesar@gmail.com' where id = 1;
-- ACTUALIZAR CON FUNCIONES
UPDATE alumno set email = CONCAT(nombre,'@gmail.com');

-- ELIMINAR
DELETE from alumno where id = 10;
