import psycopg2

def contar_vocales(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

palabra_ingresada = input('Ingrese una palabra: ')

numero_vocales = contar_vocales(palabra_ingresada)

resultado = f'La palabra {palabra_ingresada} tiene {numero_vocales} vocales.'
print(resultado)

# Escribir en el archivo
with open('ejercicio3.txt', 'w') as file:
    file.write(resultado)

# Almacenar el resultado en la variable 'salida'
salida = resultado

# Escribir en el archivo nuevamente para garantizar que ambos bloques de código hagan lo mismo
with open('ejercicio3.txt', 'w') as file:
    file.write(resultado)

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
