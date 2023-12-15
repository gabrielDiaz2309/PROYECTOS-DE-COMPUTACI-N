import psycopg2

num_str = input("Ingrese un número: ")
num = int(num_str)

divisores = [i for i in range(1, num + 1) if num % i == 0]

# Mostrar los divisores
divisores_str = "Los divisores de {} son: {}".format(num, ', '.join(map(str, divisores)))
print(divisores_str)

# Escribir en el archivo
with open("ejercicio2.txt", "w") as file:
    file.write(divisores_str)

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

    salida = divisores_str

    query = "insert into salida values (%s);"
    cursor.execute(query, (salida,))

    conn.commit()

except Exception as e:
    print("Error de conexión:", e)

finally:
    if conn is not None:
        conn.close()
