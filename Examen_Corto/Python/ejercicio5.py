# Generar números impares del 1 al 100
impares = list(range(1, 101, 2))

# Contar la cantidad de números impares
cantidad_impares = len(impares)

# Mostrar los números impares
print("Números impares:")
print(impares)

# Mostrar la cantidad de números impares
print(f"Cantidad de números impares: {cantidad_impares}")

# Almacenar en un archivo de texto
with open('ejercicio5.txt', 'w') as f:
    f.write(f'Numeros impares= {str(impares)}')
    
# Conexión a la base de datos PostgreSQL (ajusta los parámetros según tu configuración)
import psycopg2

# Establecer la conexión (ajusta los parámetros según tu configuración)
conn = psycopg2.connect(dbname='ExamenCorto1', host='localhost', port='5432', user='postgres', password='gabrielgrdb')

# Crear un cursor
cursor = conn.cursor()

# Insertar los números impares en la base de datos (ajusta la consulta según tu esquema)
query = "INSERT INTO salida VALUES (%s);"
cursor.execute(query, (impares,))

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()