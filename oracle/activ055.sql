-- 1 Dar de alta con fecha actual al empleado José Escriche Barrera como programador 
-- perteneciente al departamento de producción.  Tendrá un salario base 
-- de 70000 pts/mes y no cobrará comisión. 
insert into emp e 
(e.APELLIDO, e.OFICIO, e.DEPT_NO, e.SALARIO, e.COMISION, e.FECHA_ALT, e.EMP_NO)
values ('Jose Escriche Barrera', 'programador', 
(select d.DEPT_NO from DEPT d where d.DNOMBRE='PRODUCCIÓN'), 
70000, 0, TO_DATE('09/02/2026'), (select max(EMP_NO) from emp) +1);

-- 2 Se quiere dar de alta un departamento de informática situado en Fuenlabrada (Madrid).
INSERT into DEPT  
(DEPT_NO, DNOMBRE, LOC)
values
((select max(DEPT_NO) from DEPT)+1, 'Informática', 'Fuenlabrada(Madrid)');

-- 3 El departamento 
-- de ventas, por motivos peseteros, se traslada a Teruel, realizar dicha modificación.
update DEPT set LOC = 'Teruel' where DNOMBRE = 'VENTAS';

-- 4 En el departamento anterior (ventas), se dan de alta dos empleados: 
-- Julián Romeral y Luis Alonso.  Su salario base es el menor que cobre un empleado, y cobrarán una comisión del 15% de dicho salario.
insert into EMP (APELLIDO, OFICIO, DEPT_NO, SALARIO, COMISION, FECHA_ALT, EMP_NO)
values ('Julián Romeral', 'programador', 
(select d.DEPT_NO from DEPT d where d.DNOMBRE='VENTAS'), 
(select min(SALARIO) from EMP), ((select min(SALARIO) from EMP) * 0.15), TO_DATE('09/02/2026'), (select max(EMP_NO) from emp) +1);
insert into EMP (APELLIDO, OFICIO, DEPT_NO, SALARIO, COMISION, FECHA_ALT, EMP_NO)
values ('Luis Alonso', 'programador', 
(select d.DEPT_NO from DEPT d where d.DNOMBRE='VENTAS'), 
(select min(SALARIO) from EMP), ((select min(SALARIO) from EMP) * 0.15), TO_DATE('09/02/2026'), (select max(EMP_NO) from emp) +1);

-- 5 Modificar la comisión de los empleados de la empresa, de forma que todos tengan un incremento del 10% del salario.
update EMP set SALARIO = SALARIO + SALARIO*0.1;

-- 6 Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.
update PLANTILLA set SALARIO = SALARIO + SALARIO*0.05 where TURNO = 'N';

-- 7 Incrementar en 5000 Pts. el salario de los empleados del departamento de ventas y del presidente, tomando en cuenta los que se 
-- dieron de alta antes que el presidente de la empresa.
update emp set SALARIO = SALARIO + 5000 
where DEPT_NO = (select DEPT_NO from DEPT where DEPT.DNOMBRE = 'VENTAS') or emp.OFICIO = 'PRESIDENTE' 
and FECHA_ALT<(select FECHA_ALT from emp where emp.OFICIO = 'PRESIDENTE');

select * from EMP;


