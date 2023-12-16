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

def obtener_inventario_desde_db():
    try:
        connection = connect_to_db()
        query = "SELECT id, producto, existencia FROM inventario;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:
        print(f"Error al obtener el inventario desde la base de datos: {e}")
        return []

def obtener_existencia():
    try:
        existencia = int(input("Ingrese la existencia del producto: "))
        return existencia
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return obtener_existencia()

def agregar_producto_en_db(producto, existencia):
    try:
        connection = connect_to_db()
        query = "INSERT INTO inventario (producto, existencia) VALUES (%s, %s);"
        values = (producto, existencia)
        
        execute_query(connection, query, values)
        print("Producto agregado al inventario.")
    except Exception as e:
        print(f"Error al agregar el producto en el inventario: {e}")
    finally:
        connection.close()

def actualizar_existencia_en_db(producto_id, nueva_existencia):
    try:
        connection = connect_to_db()
        query = "UPDATE inventario SET existencia = %s WHERE id = %s;"
        values = (nueva_existencia, producto_id)
        
        execute_query(connection, query, values)
        print("Existencia actualizada en el inventario.")
    except Exception as e:
        print(f"Error al actualizar la existencia en el inventario: {e}")
    finally:
        connection.close()

def eliminar_producto_de_db(producto_id):
    try:
        connection = connect_to_db()
        query = "DELETE FROM inventario WHERE id = %s;"
        
        execute_query(connection, query, (producto_id,))
        print("Producto eliminado del inventario.")
    except Exception as e:
        print(f"Error al eliminar el producto del inventario: {e}")
    finally:
        connection.close()

def obtener_total_productos():
    try:
        connection = connect_to_db()
        query = "SELECT SUM(existencia) FROM inventario;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        total = cursor.fetchone()[0]
        
        return total
    except Exception as e:
        print(f"Error al obtener el total de productos: {e}")
        return 0

while True:
    print("Menú:")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Actualizar existencia")
    print("4. Eliminar producto")
    print("5. Ver total de productos")
    print("6. Salir")
    
    opciones_validas = ["1", "2", "3", "4", "5", "6"]
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        try:
            producto = input("Ingrese el nombre del producto: ")
            if not producto.isalpha():
                raise ValueError("Error: El nombre del producto debe ser texto.")
            
            existencia = obtener_existencia()
            agregar_producto_en_db(producto, existencia)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "2":
        inventario_desde_db = obtener_inventario_desde_db()
        print("Inventario:")
        for producto_info in inventario_desde_db:
            print(f"ID: {producto_info[0]}, Producto: {producto_info[1]}, Existencia: {producto_info[2]}")
    elif opcion == "3":
        try:
            producto_id = int(input("Ingrese el ID del producto que desea actualizar: "))
            nueva_existencia = obtener_existencia()
            actualizar_existencia_en_db(producto_id, nueva_existencia)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "4":
        try:
            producto_id = int(input("Ingrese el ID del producto que desea eliminar: "))
            eliminar_producto_de_db(producto_id)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "5":
        total_productos = obtener_total_productos()
        print(f"Total de productos en inventario: {total_productos}")
    elif opcion == "6":
        print("Saliendo del programa.")
        break
