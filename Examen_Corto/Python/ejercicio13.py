import psycopg2

# Solicitar al usuario ingresar las tres notas
nota1 = float(input('Ingrese la primera nota: '))
nota2 = float(input('Ingrese la segunda nota: '))
nota3 = float(input('Ingrese la tercera nota: '))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Verificar si el promedio es mayor o igual a 60
if promedio >= 60:
    mensaje = 'Aprobado'
else:
    mensaje = 'Reprobado'

# Crear la cadena de salida
salida = f'Promedio: {promedio:.2f}, Estado: {mensaje}'

# Mostrar en la consola
print(salida)

# Almacenar el resultado en un archivo de texto
with open('ejercicio13.txt', 'w') as archivo:
    # Escribir la cadena en el archivo
    archivo.write(salida)

# Conexión a la base de datos PostgreSQL
try:
    conn = psycopg2.connect(
        dbname='ExamenCorto1',
        host='localhost',
        port='5432',
        user='postgres',
        password='gabrielgrdb'
    )

    # Crear un cursor
    cursor = conn.cursor()

    # Ejecutar la consulta SQL
    query = f"INSERT INTO salida VALUES ('{salida}')"
    cursor.execute(query)

    # Confirmar la transacción
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    print('Resultado almacenado en "ejercicio13.txt" y en la base de datos.')
except Exception as e:
    print(f'Error al guardar en la base de datos: {e}')
