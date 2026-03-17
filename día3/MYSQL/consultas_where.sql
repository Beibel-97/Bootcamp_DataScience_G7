-- consultas select
select * from empleado;
select nombre,pais from empleado;
--ordenar
select * from empleado order by nombre;
select * from empleado order by salario desc;

-- filtros
select * from empleado where pais = 'Peru';
select * from empleado where salario > 5000;
select * from empleado where salario between 1000 and 3000;
select * from empleado
where pais = 'Peru' or pais = 'Chile' and salario > 5000;
select * from empleado
where pais in ('Peru','Colombia','Chile');