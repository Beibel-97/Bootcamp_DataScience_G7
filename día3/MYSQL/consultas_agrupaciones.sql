-- FUNCIONES
select count(*) as total_empleados from empleado;
select count(*) as total_mayor_5000 from empleado
where salario > 5000;

select max(salario),min(salario),avg(salario) from empleado;
-- valores unicos
select distinct pais from empleado;

--AGRUPACIONES
--SELECCIONAR TOTAL DE EMPLEADOS POR PAIS
select pais,count(*) as total_empleados from empleado
group by pais
order by count(*) desc;

select pais,area,max(salario) from empleado
group by pais,area;

-- subconsultas
-- consultas todos los empleados cuyo salario es mayor al promedio
select avg(salario) from empleado;
select nombre,salario from empleado
where salario > (select avg(salario) from empleado);

select e.pais,count(e.id) as total,
(select avg(promedio_empleado.salario) 
from empleado promedio_empleado where promedio_empleado.pais = e.pais) as salario_promedio
from empleado e
group by e.pais order by count(e.id);

select avg(promedio_empleado.salario) 
from empleado promedio_empleado where promedio_empleado.pais = 'Uruguay'