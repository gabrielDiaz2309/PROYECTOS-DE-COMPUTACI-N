import psycopg2

numero = int(input("Ingrese un número: "))

suma = sum(range(1, numero + 1))
numeros = "+".join(map(str, range(1, numero + 1)))

salida = f"Numero {numero} : {numeros} = {suma}"
print(salida)

# Escribir en el archivo
with open("ejercicio7.txt", "w") as file:
    file.write(salida)

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

    query = "insert into salida values (%s);"
    cursor.execute(query, (salida,))

    conn.commit()

except Exception as e:
    print("Error de conexión:", e)

finally:
    if conn is not None:
        conn.close()
