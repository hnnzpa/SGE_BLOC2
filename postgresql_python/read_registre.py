import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * from clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()
    #print(results)
    #print(results[4])
    #print(results[4][0], results[4][4]) # de part meva el nom

    print(results)
    for i in range (len(results)):
        if results[i][0] == 'Andreu':
            print(i)
            print(results[i])
            print(results[i][3])

    for i in range (len(results)):
        if results[i][0] == 'Vivian':
            print(i)
            print(results[i])
            print(results[i][1])

    for i in range (len(results)):
        if results[i][0] == 'Albert':
            print(i)
            print(results[i])
            print(results[i][4])


    return results

read_reg()
