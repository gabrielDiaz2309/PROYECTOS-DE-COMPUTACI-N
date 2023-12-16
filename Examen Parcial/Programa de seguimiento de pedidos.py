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

# Función para obtener el estado de pedido válido
def obtener_estado_pedido():
    while True:
        estado = input("Ingrese el estado del pedido (en curso/entregado): ").lower()
        if estado in ["en curso", "entregado"]:
            return estado
        else:
            print("Estado inválido. Por favor, ingrese 'en curso' o 'entregado'.")

def agregar_pedido_en_db(pedido, estado):
    try:
        connection = connect_to_db()
        query = "INSERT INTO pedidos (pedido, estado) VALUES (%s, %s);"
        values = (pedido, estado)
        
        execute_query(connection, query, values)
        print("Pedido agregado a la base de datos.")
    except Exception as e:
        print(f"Error al agregar el pedido en la base de datos: {e}")
    finally:
        connection.close()

def actualizar_estado_pedido_en_db(pedido_id, nuevo_estado):
    try:
        connection = connect_to_db()
        query = "UPDATE pedidos SET estado = %s WHERE id = %s;"
        values = (nuevo_estado, pedido_id)
        
        execute_query(connection, query, values)
        print("Estado de pedido actualizado en la base de datos.")
    except Exception as e:
        print(f"Error al actualizar el estado del pedido en la base de datos: {e}")
    finally:
        connection.close()

def eliminar_pedido_de_db(pedido_id):
    try:
        connection = connect_to_db()
        query = "DELETE FROM pedidos WHERE id = %s;"
        
        execute_query(connection, query, (pedido_id,))
        print("Pedido eliminado de la base de datos.")
    except Exception as e:
        print(f"Error al eliminar el pedido de la base de datos: {e}")
    finally:
        connection.close()

def obtener_pedidos_desde_db():
    try:
        connection = connect_to_db()
        query = "SELECT id, pedido, estado FROM pedidos;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:
        print(f"Error al obtener los pedidos desde la base de datos: {e}")
        return []

while True:
    print("Menú:")
    print("1. Agregar pedido")
    print("2. Ver pedidos")
    print("3. Actualizar estado de pedido")
    print("4. Eliminar pedido")
    print("5. Salir")
    
    opciones_validas = ["1", "2", "3", "4", "5"]
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        try:
            pedido = input("Ingrese la descripción del pedido: ")
            estado = obtener_estado_pedido()
            agregar_pedido_en_db(pedido, estado)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "2":
        pedidos_desde_db = obtener_pedidos_desde_db()
        print("Pedidos:")
        for pedido_info in pedidos_desde_db:
            print(f"ID: {pedido_info[0]}, Pedido: {pedido_info[1]}, Estado: {pedido_info[2]}")
    elif opcion == "3":
        try:
            pedido_id = int(input("Ingrese el ID del pedido que desea actualizar: "))
            nuevo_estado = obtener_estado_pedido()
            actualizar_estado_pedido_en_db(pedido_id, nuevo_estado)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "4":
        try:
            pedido_id = int(input("Ingrese el ID del pedido que desea eliminar: "))
            eliminar_pedido_de_db(pedido_id)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "5":
        print("Saliendo del programa.")
        break
