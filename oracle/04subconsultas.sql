select max(SALARIO) from EMP;

select * from EMP where SALARIO = 650000;

select * from EMP where SALARIO = (select max(SALARIO) from EMP);

select * 
from EMP 
where OFICIO = (
    select OFICIO 
    from EMP 
    where APELLIDO = 'alonso');

select emp.APELLIDO
from EMP emp
where emp.SALARIO > (
    select SALARIO
    from EMP 
    where emp.SALARIO > (select SALARIO from EMP where APELLIDO = 'sala'));

select * 
from EMP 
where OFICIO = (
    select OFICIO 
    from EMP 
    where APELLIDO = 'alonso') 
    or (
    OFICIO = (
        select OFICIO 
        from EMP 
        where APELLIDO = 'jimenez')
    );

select * 
from EMP 
where OFICIO IN (
    select OFICIO 
    from EMP 
    where APELLIDO = 'alonso'
    or APELLIDO = 'jimenez'
    )
    and 
    ROWNUM <= 5
order by EMP.EMP_NO desc;

select APELLIDO, oficio, SALARIO from EMP
union 
select d.APELLIDO, d.ESPECIALIDAD, d.SALARIO from doctor d
union 
select p.APELLIDO, p.funcion, p.SALARIO from plantilla p;

select *
    from (select * 
        from (
            select APELLIDO, oficio, SALARIO 
            from EMP
            union 
            select d.APELLIDO, d.ESPECIALIDAD, d.SALARIO 
            from doctor d
            union 
            select p.APELLIDO, p.funcion, p.SALARIO 
            from plantilla p
        ) unidos
        where SALARIO > 300000
        order by SALARIO desc
        )
where ROWNUM <= 3;

select APELLIDO, funcion,
case TURNO
    when 'M' then 'mañana'
    when 'T' then 'tarde'
    when 'N' then 'noche'
end as turno
from plantilla;

--1
select e.EMP_NO, e.APELLIDO, e.FECHA_ALT
from EMP e
order by e.FECHA_ALT 
fetch first 1 rows only;

--2
select e.EMP_NO, e.APELLIDO, e.FECHA_ALT
from EMP e
order by e.FECHA_ALT desc
fetch first 1 rows only;

--3
select APELLIDO, SALARIO
from EMP
where OFICIO = (
    select OFICIO
    from EMP 
    where APELLIDO = 'jimenez'
    );

--4
select APELLIDO, OFICIO, SALARIO, DEPT_NO
from EMP
where SALARIO > (
    select max(SALARIO)
    from EMP 
    where EMP.DEPT_NO = 30
    );

--5
select APELLIDO, OFICIO, DEPT_NO
from EMP
union 
select APELLIDO, FUNCION, SALA_COD
from PLANTILLA;

--6
select APELLIDO, OFICIO
from EMP 
where OFICIO = (
    select OFICIO
    from DEPT
    where DNOMBRE = 'VENTAS'
)
and DEPT_NO = 20;

--7
select * 
from emp 
where salario > (
    select avg(SALARIO) 
    from emp 
    where OFICIO = 'DIRECTOR'
    )
and OFICIO <> 'PRESIDENTE';

--8
select APELLIDO, FUNCION, SALARIO, p.HOSPITAL_COD
from plantilla p
join HOSPITAL h on p.HOSPITAL_COD = h.HOSPITAL_COD
where p.FUNCION IN ('ENFERMERO', 'ENFERMERA')
and h.NOMBRE = 'san carlos';

--9
select *
from(
select  APELLIDO, OFICIO, SALARIO
from EMP
union 
select APELLIDO, FUNCION, SALARIO
from PLANTILLA
UNION
select APELLIDO, ESPECIALIDAD, SALARIO
from DOCTOR
) associados
order by SALARIO desc;

--10
select *
from(
select  APELLIDO, OFICIO, SALARIO
from EMP
union 
select APELLIDO, FUNCION, SALARIO
from PLANTILLA
UNION
select APELLIDO, ESPECIALIDAD, SALARIO
from DOCTOR
) associados
where OFICIO like '%O'
order by SALARIO desc;

--11
select HOSPITAL.HOSPITAL_COD, HOSPITAL.DIRECCION, HOSPITAL.NOMBRE, HOSPITAL.NUM_CAMA, HOSPITAL.TELEFONO
from HOSPITAL
join DOCTOR on HOSPITAL.HOSPITAL_COD = DOCTOR.HOSPITAL_COD
where DOCTOR.ESPECIALIDAD like 'Cardiologia';

--12
select p.APELLIDO, p.SALARIO*14 as salarioAnual
from plantilla p
join HOSPITAL h on p.HOSPITAL_COD = h.HOSPITAL_COD
where h.NOMBRE in ('provincial', 'general');

--12
select e.APELLIDO
from ENFERMO e
where e.FECHA_NAC > (
    select e2.FECHA_NAC
    from ENFERMO e2
    where e2.APELLIDO like 'Miller G.'
);

--13
select *
from(
select oficio, max(SALARIO), avg(SALARIO), sum(SALARIO), min(SALARIO), count(*)
from EMP
group by oficio
union 
select funcion, max(SALARIO), avg(SALARIO), sum(SALARIO), min(SALARIO), count(*)
from PLANTILLA
group by funcion
UNION 
select especialidad, max(SALARIO), avg(SALARIO), sum(SALARIO), min(SALARIO), count(*)
from DOCTOR
group by especialidad
) resumen;
