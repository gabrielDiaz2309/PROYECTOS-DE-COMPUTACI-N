import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# Función para conectarse a la base de datos PostgreSQL
def connect_to_db():
    connection = psycopg2.connect(
        host="localhost",
        database="examen1",
        user="postgres",
        password="gabrielgrdb"
    )
    return connection

# Función para ejecutar una consulta en la base de datos
def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    connection.commit()
    cursor.close()

# Función para simular datos aleatorios de sensores
def generar_datos_aleatorios():
    temperatura = np.random.uniform(-10, 30)
    humedad = np.random.uniform(0, 100)
    return temperatura, humedad

# Función para agregar datos de sensores a la base de datos
def agregar_datos_sensor_en_db(temperatura, humedad):
    try:
        connection = connect_to_db()
        query = "INSERT INTO sensores (temperatura, humedad) VALUES (%s, %s);"
        values = (temperatura, humedad)
        
        execute_query(connection, query, values)
        print("Datos del sensor agregados a la base de datos.")
    except Exception as e:
        print(f"Error al agregar los datos del sensor en la base de datos: {e}")
    finally:
        connection.close()

# Función para generar y mostrar gráficos y tablas de análisis de sensores
def analizar_sensores():
    try:
        connection = connect_to_db()
        query = "SELECT temperatura, humedad FROM sensores;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()

        if not resultados:
            print("No hay datos de sensores para analizar.")
            return

        # Extracción de datos para los gráficos
        temperaturas = [resultado[0] for resultado in resultados]
        humedades = [resultado[1] for resultado in resultados]

        # Gráfico de puntos para temperatura
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(range(1, len(temperaturas) + 1), temperaturas, marker='o', linestyle='-', color='r')
        plt.title('Gráfico de Temperatura')
        plt.xlabel('ID')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)

        # Gráfico de puntos para humedad
        plt.subplot(1, 2, 2)
        plt.plot(range(1, len(humedades) + 1), humedades, marker='o', linestyle='-', color='b')
        plt.title('Gráfico de Humedad')
        plt.xlabel('ID')
        plt.ylabel('Humedad (%)')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        # Tabla de datos
        print("\nTabla de Datos:")
        print("ID\tTemperatura\tHumedad")
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}\t{resultado[0]}\t\t{resultado[1]}")

    except Exception as e:
        print(f"Error al analizar los datos de sensores desde la base de datos: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    while True:
        print("\nMenú:")
        print("1. Agregar datos de sensores")
        print("2. Analizar sensores")
        print("3. Salir")

        opciones_validas = ["1", "2", "3"]
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                temperatura, humedad = generar_datos_aleatorios()
                agregar_datos_sensor_en_db(temperatura, humedad)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            analizar_sensores()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
