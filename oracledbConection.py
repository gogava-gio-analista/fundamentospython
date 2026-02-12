import oracledb 
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
dsn = os.getenv('dsn')
coneccion = oracledb.connect(user=user, password=password, dsn=dsn)
cursor = coneccion.cursor()

def consulta(sql):
    cursor.execute(sql)

    if sql.strip().lower().startswith("select"):
        for row in cursor:
            print(row)
        return row
    else:
        existencia = input('quieres guardar cambios? ').lower().replace('í', 'i').strip()
        if existencia:
            print("filas afectadas:", cursor.rowcount)
            coneccion.commit()
            print('Cambios guardado.')
        else:
            coneccion.rollback()
            print('cambios no guardados')
    cursor.close()
    coneccion.close()