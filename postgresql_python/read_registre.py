import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * from clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()
    print(results)

    return results

read_reg()
