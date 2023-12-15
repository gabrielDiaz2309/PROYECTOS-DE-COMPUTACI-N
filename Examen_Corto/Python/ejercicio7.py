import math
import psycopg2

numero = int(input('Ingrese un número: '))

if numero % 7 == 0:
    # Calcular el factorial si el número es divisible por 7
    factorial_resultado = math.factorial(numero)
    print(f'El factorial de {numero} es: {factorial_resultado}')

    # Almacenar el resultado en el archivo de texto
    nombre_archivo = 'ejercicio7.txt'
    with open(nombre_archivo, 'w') as file:
        file.write(f'El factorial de {numero} es: {factorial_resultado}\n')
    print(f'El resultado se ha guardado en {nombre_archivo}')

    # Almacenar el resultado en la variable 'salida'
    salida = str(factorial_resultado)

    # Conexión a la base de datos PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname='ExamenCorto1',
            host='localhost',
            port='5432',
            user='postgres',
            password='gabrielgrdb'
        )

        cursor = conn.cursor()
        query = f"INSERT INTO salida VALUES ('{salida}')"
        cursor.execute(query)
        conn.commit()

        print('El resultado se ha insertado en la base de datos.')

    except psycopg2.Error as e:
        print(f'Error al insertar en la base de datos: {e}')

    finally:
        if conn:
            cursor.close()
            conn.close()

else:
    print('Error: El número no es divisible por 7.')
