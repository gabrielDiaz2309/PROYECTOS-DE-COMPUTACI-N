import psycopg2

print("Ingrese el primer número")
Num1 = float(input())

print("Ingrese el segundo número")
Num2 = float(input())

print("Ingrese el tercer número")
Num3 = float(input())

if Num1 == Num2 == Num3:
    Res = "Todos son iguales: {:.2f}".format(Num1)
elif Num1 == Num2:
    Res = "El número diferente es: {:.2f}".format(Num3)
elif Num1 == Num3:
    Res = "El número diferente es: {:.2f}".format(Num2)
elif Num2 == Num3:
    Res = "El número diferente es: {:.2f}".format(Num1)
elif Num1 > Num2 and Num1 > Num3:
    Res = "La suma de los números es: {:.2f}".format(Num1 + Num2 + Num3)
elif Num2 > Num1 and Num2 > Num3:
    Res = "La multiplicación de los números es: {:.2f}".format(Num1 * Num2 * Num3)
else:
    Res = "La concatenación es: {}".format(str(int(Num1)) + str(int(Num2)) + str(int(Num3)))

print(Res)

# Escribir en el archivo
with open("ejercicio1.txt", "w") as file:
    file.write(Res)

# Conexión a la base de datos PostgreSQL
try:
    conn = psycopg2.connect(
        dbname='ExamenCorto1',
        user='postgres',
        password='gabrielgrdb',
        host='localhost',
        port='5432'
    )

    cursor = conn.cursor()

    salida = Res

    query = "insert into salida values (%s);"
    cursor.execute(query, (salida,))

    conn.commit()

except Exception as e:
    print("Error de conexión:", e)

finally:
    if conn is not None:
        conn.close()
