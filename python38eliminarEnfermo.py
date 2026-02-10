from oracledbConection import consulta

numInscripcion = int(input('dime el numero de inscripcion que quieras eliminar: '))
sql = f'delete from enfermo where inscripcion = {numInscripcion}'

consulta(sql)
