select DISTINCT DEPT_NO from EMP;
select * from DEPT;

select e.APELLIDO, e.OFICIO, e.DEPT_NO, d.DNOMBRE, d.DEPT_NO, d.LOC  from EMP e
full join DEPT d
on e.DEPT_NO = d.DEPT_NO;

select sum(SALARIO) as sumaSalarial, h.NOMBRE
from PLANTILLA p 
join HOSPITAL h
on p.HOSPITAL_COD = h.HOSPITAL_COD
group by h.NOMBRE;

select count(e.EMP_NO) as numeroEmpleados, d.LOC
from EMP e
right join DEPT d
on e.DEPT_NO = d.DEPT_NO
group by d.LOC;

select p.APELLIDO, p.FUNCION, h.NOMBRE, h.DIRECCION, s.NOMBRE
from HOSPITAL h
join PLANTILLA p
on h.HOSPITAL_COD = p.HOSPITAL_COD
join SALA s
on s.HOSPITAL_COD = h.HOSPITAL_COD
and s.SALA_COD = p.SALA_COD;

select * from PLANTILLA;

select h.NOMBRE, s.NOMBRE
from HOSPITAL h
left join SALA s
on h.HOSPITAL_COD = s.HOSPITAL_COD;

select d.DNOMBRE, count(e.EMP_NO) as numeroEmpleados, e.OFICIO
from DEPT d
join EMP e
on d.DEPT_NO = e.DEPT_NO
group by d.DNOMBRE, e.OFICIO;

select count(s.SALA_COD) as numeroSalas, s.NOMBRE as SALA, h.NOMBRE
from SALA s
join HOSPITAL h
on s.HOSPITAL_COD = h.HOSPITAL_COD
group by s.NOMBRE, h.NOMBRE;

select count(e.EMP_NO) as ALTAS, d.DNOMBRE
from EMP e
join DEPT d
on e.DEPT_NO = d.DEPT_NO
where e.FECHA_ALT between '01-01-1997' and '31-12-1998'
group by d.DNOMBRE;

select d.LOC as CIUDAD, count(e.EMP_NO) as PERSONAS 
from EMP e
join DEPT d
on e.DEPT_NO = d.DEPT_NO
group by d.LOC
having count(e.EMP_NO) > 4;

select sum(e.SALARIO)/count(e.EMP_NO) as MEDIA_SALARIAL, d.LOC as CIUDAD
from EMP e
join DEPT d
on e.DEPT_NO = d.DEPT_NO
where d.LOC in ('MADRID', 'SEVILLA')
group by d.LOC;

select d.APELLIDO, h.NOMBRE, h.DIRECCION, h.TELEFONO
from HOSPITAL h
join DOCTOR d
on h.HOSPITAL_COD = d.HOSPITAL_COD;

select max(p.SALARIO) as SALARIO_MAXIMO, h.NOMBRE
from HOSPITAL h
join PLANTILLA p
on h.HOSPITAL_COD = p.HOSPITAL_COD
group by h.NOMBRE
order by SALARIO_MAXIMO desc;

select p.APELLIDO, p.FUNCION, p.TURNO, s.NOMBRE, h.NOMBRE
from PLANTILLA p
join HOSPITAL h
on p.HOSPITAL_COD = h.HOSPITAL_COD
join SALA s
on s.HOSPITAL_COD = h.HOSPITAL_COD
and s.SALA_COD = p.SALA_COD;

select distinct s.NOMBRE as nombreSala, h.NOMBRE as nombreHospital
from SALA s
cross join HOSPITAL h;