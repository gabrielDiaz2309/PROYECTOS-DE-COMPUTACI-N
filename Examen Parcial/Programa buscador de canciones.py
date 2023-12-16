import psycopg2

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

# Función para agregar una canción a la base de datos
def agregar_cancion_en_db(artista, cancion, letra):
    try:
        connection = connect_to_db()
        
        query = "INSERT INTO musica (artista, cancion, letra) VALUES (%s, %s, %s);"
        values = (artista, cancion, letra)
        
        execute_query(connection, query, values)
        print("Canción agregada a la base de datos.")
    except Exception as e:
        print(f"Error al agregar la canción en la base de datos: {e}")
    finally:
        connection.close()

# Función para desplegar el listado de canciones
def desplegar_listado_canciones():
    try:
        connection = connect_to_db()
        query = "SELECT id, artista, cancion, letra FROM musica;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        canciones = cursor.fetchall()
        
        if canciones:
            print("Listado de Canciones:")
            for cancion in canciones:
                print(f"{cancion[0]}. Artista: {cancion[1]}, Canción: {cancion[2]}\nLetra: {cancion[3]}\n")
        else:
            print("No hay canciones disponibles.")
    except Exception as e:
        print(f"Error al desplegar el listado de canciones: {e}")
    finally:
        connection.close()

# Función para buscar por artista
def buscar_por_artista(artista):
    try:
        connection = connect_to_db()
        query = "SELECT id, artista, cancion, letra FROM musica WHERE artista ILIKE %s;"
        
        cursor = connection.cursor()
        cursor.execute(query, (f"%{artista}%",))
        canciones = cursor.fetchall()
        
        if canciones:
            print(f"Canciones de {artista}:")
            for cancion in canciones:
                print(f"{cancion[0]}. Canción: {cancion[2]}\nLetra: {cancion[3]}\n")
        else:
            print(f"No hay canciones de {artista} disponibles.")
    except Exception as e:
        print(f"Error al buscar por artista: {e}")
    finally:
        connection.close()

# Función para buscar por canción
def buscar_por_cancion(cancion):
    try:
        connection = connect_to_db()
        query = "SELECT id, artista, cancion, letra FROM musica WHERE cancion ILIKE %s;"
        
        cursor = connection.cursor()
        cursor.execute(query, (f"%{cancion}%",))
        canciones = cursor.fetchall()
        
        if canciones:
            print(f"Canciones con el nombre {cancion}:")
            for cancion in canciones:
                print(f"{cancion[0]}. Artista: {cancion[1]}, Canción: {cancion[2]}\nLetra: {cancion[3]}\n")
        else:
            print(f"No hay canciones con el nombre {cancion} disponibles.")
    except Exception as e:
        print(f"Error al buscar por canción: {e}")
    finally:
        connection.close()

# Menú del buscador de canciones
while True:
    print("Buscador de Canciones:")
    print("1. Desplegar el listado de canciones")
    print("2. Buscar por artista")
    print("3. Buscar por canción")
    print("4. Agregar nueva canción")
    print("5. Salir")
    
    opciones_validas = ["1", "2", "3", "4", "5"]
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        desplegar_listado_canciones()
    elif opcion == "2":
        artista = input("Ingrese el nombre del artista: ")
        buscar_por_artista(artista)
    elif opcion == "3":
        cancion = input("Ingrese el nombre de la canción: ")
        buscar_por_cancion(cancion)
    elif opcion == "4":
        artista = input("Ingrese el nombre del artista de la nueva canción: ")
        cancion = input("Ingrese el nombre de la nueva canción: ")
        letra = input("Ingrese la letra de la nueva canción: ")
        agregar_cancion_en_db(artista, cancion, letra)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
