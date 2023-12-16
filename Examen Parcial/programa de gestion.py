import psycopg2

# Función para conectar a la base de datos PostgreSQL
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

def agregar_producto_en_db(producto, cantidad, precio_unitario):
    try:
        connection = connect_to_db()
        query = "INSERT INTO gestion (producto, cantidad, precio_unitario) VALUES (%s, %s, %s);"
        values = (producto, cantidad, precio_unitario)

        execute_query(connection, query, values)
        print("Producto agregado al inventario.")
    except Exception as e:
        print(f"Error al agregar el producto al inventario: {e}")
    finally:
        connection.close()

def mostrar_productos():
    try:
        connection = connect_to_db()
        query = "SELECT id, producto FROM gestion;"

        cursor = connection.cursor()
        cursor.execute(query)
        productos = cursor.fetchall()

        print("Productos en el inventario:")
        for producto in productos:
            print(f"ID: {producto[0]}, Producto: {producto[1]}")

        return productos
    except Exception as e:
        print(f"Error al obtener la lista de productos: {e}")
        return []

def actualizar_inventario():
    try:
        productos = mostrar_productos()
        if not productos:
            return

        producto_id = int(input("Ingrese el ID del producto que desea actualizar: "))
        cantidad = int(input("Ingrese la nueva cantidad en inventario: "))

        connection = connect_to_db()
        query = "UPDATE gestion SET cantidad = %s WHERE id = %s;"
        values = (cantidad, producto_id)

        execute_query(connection, query, values)
        print("Inventario actualizado.")
    except Exception as e:
        print(f"Error al actualizar el inventario: {e}")
    finally:
        connection.close()

def generar_informe_inventario():
    try:
        connection = connect_to_db()
        query = "SELECT id, producto, cantidad, precio_unitario FROM gestion;"

        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()

        return resultados
    except Exception as e:
        print(f"Error al generar el informe de inventario desde la base de datos: {e}")
        return []

while True:
    print("Menú:")
    print("1. Agregar producto al inventario")
    print("2. Actualizar inventario")
    print("3. Generar informe de inventario")
    print("4. Salir")

    opciones_validas = ["1", "2", "3", "4"]
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad en inventario: "))
            precio_unitario = float(input("Ingrese el precio unitario: "))
            agregar_producto_en_db(producto, cantidad, precio_unitario)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "2":
        actualizar_inventario()
    elif opcion == "3":
        informe_inventario = generar_informe_inventario()
        print("Informe de inventario:")
        for producto_info in informe_inventario:
            print(f"ID: {producto_info[0]}, Producto: {producto_info[1]}, Cantidad: {producto_info[2]}, Precio Unitario: {producto_info[3]}")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
