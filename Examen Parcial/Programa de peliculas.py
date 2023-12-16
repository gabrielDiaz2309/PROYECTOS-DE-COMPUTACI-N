import psycopg2

# Lista de géneros válidos
generos_validos = ["Romance", "Drama", "Ciencia Ficción", "Crimen", "Acción", "Aventura"]

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

# Función para agregar una película a la base de datos
def agregar_pelicula_en_db(nombre, genero):
    try:
        connection = connect_to_db()
        
        # Verificar si el género es válido
        if genero not in generos_validos:
            raise ValueError("Género no válido. Por favor, elija un género de la lista.")
        
        query = "INSERT INTO peliculas (nombre, genero) VALUES (%s, %s);"
        values = (nombre, genero)
        
        execute_query(connection, query, values)
        print("Película agregada a la base de datos.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error al agregar la película en la base de datos: {e}")
    finally:
        connection.close()

# Función para generar recomendaciones de películas
def recomendar_peliculas(genero):
    try:
        connection = connect_to_db()
        
        # Verificar si el género es válido
        if genero not in generos_validos:
            raise ValueError("Género no válido. Por favor, elija un género de la lista.")
        
        query = "SELECT nombre FROM peliculas WHERE genero = %s;"
        
        cursor = connection.cursor()
        cursor.execute(query, (genero,))
        resultados = cursor.fetchall()
        
        return resultados
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"Error al generar recomendaciones desde la base de datos: {e}")
        return []

# Menú principal del sistema de recomendación
while True:
    print("Sistema de Recomendación de Películas:")
    print("1. Ingresar nueva película")
    print("2. Obtener recomendaciones")
    print("3. Salir")
    
    opciones_validas = ["1", "2", "3"]
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        try:
            nombre = input("Ingrese el nombre de la película: ")
            genero = input("Ingrese el género de la película (Romance, Drama, Ciencia Ficción, Crimen, Acción, Aventura): ")
            agregar_pelicula_en_db(nombre, genero)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "2":
        genero_usuario = input("Ingrese su género de película favorito (Romance, Drama, Ciencia Ficción, Crimen, Acción, Aventura): ")
        recomendaciones = recomendar_peliculas(genero_usuario)
        if recomendaciones:
            print("Películas recomendadas:")
            for pelicula in recomendaciones:
                print(pelicula[0])
        else:
            print("No hay recomendaciones disponibles.")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
