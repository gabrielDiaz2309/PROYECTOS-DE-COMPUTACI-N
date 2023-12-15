import psycopg2

# Solicitar al usuario ingresar el año de nacimiento
anno_nacimiento = int(input("Ingrese el año de nacimiento: "))

# Verificar si el año es bisiesto
if (anno_nacimiento % 4 == 0 and anno_nacimiento % 100 != 0) or anno_nacimiento % 400 == 0:
    resultado = f"El año {anno_nacimiento} es bisiesto."
else:
    resultado = f"El año {anno_nacimiento} no es bisiesto."

# Almacenar el resultado en una variable llamada salida
salida = resultado

# Guardar el resultado en un archivo de texto
nombre_archivo = "ejercicio14.txt"
with open(nombre_archivo, 'w') as fid:
    fid.write(salida)

print(f"Resultado: {salida}")
print(f"El resultado ha sido guardado en el archivo {nombre_archivo}")

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

    print('Resultado almacenado en "ejercicio14.txt" y en la base de datos.')
except Exception as e:
    print(f'Error al guardar en la base de datos: {e}')
