# És un arxiu que servirà per crear la taula amb els camps (sense registres) segons l’arxiu .csv (clientes).

import psycopg2

def create_tables():
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    sql_clientes = '''
        CREATE TABLE Clientes (
        Nombre_Cliente VARCHAR(100),
        Dirección_Cliente VARCHAR(200),
        Teléfono_Cliente VARCHAR(100),
        Correo_Electrónico_Cliente VARCHAR(100),
        Fecha_Cumpleaños VARCHAR(100);
        '''

    cursor.execute(sql_clientes)

    conn.commit()

    conn.close()
    cursor.close()

    return {"Tables created succesfully"}