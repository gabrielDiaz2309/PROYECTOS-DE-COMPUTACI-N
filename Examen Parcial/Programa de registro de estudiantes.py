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

class Estudiante:
    def __init__(self, id, nombre, edad, genero, direccion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion

def obtener_informacion_estudiante():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        
        if any(c.isdigit() for c in nombre):
            raise ValueError("El nombre no debe contener números.")
        
        edad = None
        while edad is None:
            try:
                edad = int(input("Ingrese la edad del estudiante: "))
            except ValueError:
                print("Error: La edad debe ser un número entero.")
        
        genero = input("Ingrese el género del estudiante (Femenino/Masculino/Otros): ").capitalize()
        if genero not in ["Femenino", "Masculino", "Otros"]:
            raise ValueError("Género inválido. Debe ser Femenino, Masculino u Otros.")
        
        direccion = input("Ingrese la dirección del estudiante: ")
        
        return Estudiante(None, nombre, edad, genero, direccion)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def insertar_estudiante_en_db(estudiante):
    try:
        connection = connect_to_db()
        query = "INSERT INTO estudiantes (nombre, edad, genero, direccion) VALUES (%s, %s, %s, %s) RETURNING id;"
        values = (estudiante.nombre, estudiante.edad, estudiante.genero, estudiante.direccion)
        
        cursor = connection.cursor()
        cursor.execute(query, values)
        estudiante_id = cursor.fetchone()[0]
        
        connection.commit()
        cursor.close()
        
        estudiante.id = estudiante_id  # Asignar el ID de la base de datos al estudiante
        estudiantes.append(estudiante)  # Agregar el estudiante al historial en memoria
        print("Estudiante insertado en la base de datos.")
    except Exception as e:
        print(f"Error al insertar el estudiante en la base de datos: {e}")
    finally:
        connection.close()

def obtener_estudiantes_desde_db():
    try:
        connection = connect_to_db()
        query = "SELECT id, nombre, edad, genero, direccion FROM estudiantes;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        estudiantes = []
        
        for result in resultados:
            estudiantes.append(Estudiante(result[0], result[1], result[2], result[3], result[4]))
        
        return estudiantes
    except Exception as e:
        print(f"Error al obtener los estudiantes desde la base de datos: {e}")
        return []
    finally:
        connection.close()

def insertar_estudiante_en_db(estudiante):
    try:
        connection = connect_to_db()
        query = "INSERT INTO estudiantes (nombre, edad, genero, direccion) VALUES (%s, %s, %s, %s) RETURNING id;"
        values = (estudiante.nombre, estudiante.edad, estudiante.genero, estudiante.direccion)
        
        cursor = connection.cursor()
        cursor.execute(query, values)
        estudiante_id = cursor.fetchone()[0]
        
        connection.commit()
        cursor.close()
        
        estudiante.id = estudiante_id  # Asignar el ID de la base de datos al estudiante
        estudiantes.append(estudiante)  # Agregar el estudiante al historial en memoria
        print("Estudiante insertado en la base de datos.")
    except Exception as e:
        print(f"Error al insertar el estudiante en la base de datos: {e}")
    finally:
        connection.close()

def eliminar_estudiante_de_db(estudiante_id):
    try:
        connection = connect_to_db()
        query = "DELETE FROM estudiantes WHERE id = %s;"
        
        execute_query(connection, query, (estudiante_id,))
        
        # Actualizar el historial en memoria eliminando el estudiante correspondiente
        estudiante_a_eliminar = next((estudiante for estudiante in estudiantes if estudiante.id == estudiante_id), None)
        if estudiante_a_eliminar:
            estudiantes.remove(estudiante_a_eliminar)
        
        print("Estudiante eliminado de la base de datos.")
    except Exception as e:
        print(f"Error al eliminar el estudiante de la base de datos: {e}")
    finally:
        connection.close()

def buscar_estudiante_por_id(estudiante_id):
    try:
        connection = connect_to_db()
        query = "SELECT id, nombre, edad, genero, direccion FROM estudiantes WHERE id = %s;"
        
        cursor = connection.cursor()
        cursor.execute(query, (estudiante_id,))
        result = cursor.fetchone()
        
        if result:
            return Estudiante(result[0], result[1], result[2], result[3], result[4])
        else:
            print("No se encontró un estudiante con ese ID.")
            return None
    except Exception as e:
        print(f"Error al buscar el estudiante en la base de datos: {e}")
        return None
    finally:
        connection.close()

def editar_estudiante_en_db(estudiante):
    try:
        connection = connect_to_db()
        query = "UPDATE estudiantes SET nombre=%s, edad=%s, genero=%s, direccion=%s WHERE id=%s;"
        values = (estudiante.nombre, estudiante.edad, estudiante.genero, estudiante.direccion, estudiante.id)

        execute_query(connection, query, values)

        # Actualizar el historial en memoria con el estudiante editado
        indice_estudiante = next((i for i, est in enumerate(estudiantes) if est.id == estudiante.id), None)
        if indice_estudiante is not None:
            estudiantes[indice_estudiante] = estudiante

        print("Estudiante editado en la base de datos.")
    except Exception as e:
        print(f"Error al editar el estudiante en la base de datos: {e}")
    finally:
        connection.close()

estudiantes = obtener_estudiantes_desde_db()

while True:
    print("Menú:")
    print("1. Agregar estudiante")
    print("2. Ver historial")
    print("3. Editar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        estudiante = obtener_informacion_estudiante()
        if estudiante:
            insertar_estudiante_en_db(estudiante)
    elif opcion == "2":
        print("Historial de estudiantes:")
        for idx, estudiante in enumerate(estudiantes, start=1):
            print(f"Estudiante {idx}:")
            print(f"ID: {estudiante.id}")
            print(f"Nombre: {estudiante.nombre}")
            print(f"Edad: {estudiante.edad}")
            print(f"Género: {estudiante.genero}")
            print(f"Dirección: {estudiante.direccion}")
            print("----------------------")
    elif opcion == "3":
        estudiante_id = int(input("Ingrese el ID del estudiante que desea editar: "))
        estudiante = buscar_estudiante_por_id(estudiante_id)
        if estudiante:
            print(f"Editando al estudiante con ID: {estudiante.id}")
            nuevo_estudiante = obtener_informacion_estudiante()
            if nuevo_estudiante:
                nuevo_estudiante.id = estudiante.id
                editar_estudiante_en_db(nuevo_estudiante)
    elif opcion == "4":
        estudiante_id = int(input("Ingrese el ID del estudiante que desea eliminar: "))
        estudiante = buscar_estudiante_por_id(estudiante_id)
        if estudiante:
            eliminar_estudiante_de_db(estudiante_id)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
