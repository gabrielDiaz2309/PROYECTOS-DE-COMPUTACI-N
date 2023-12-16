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

def obtener_presupuesto_inicial():
    try:
        presupuesto = float(input("Ingrese el presupuesto inicial: "))
        return presupuesto
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return obtener_presupuesto_inicial()

def obtener_gasto():
    try:
        gasto = float(input("Ingrese el monto del gasto: "))
        return gasto
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return obtener_gasto()

def agregar_gasto(presupuesto, gasto):
    nuevo_presupuesto = presupuesto - gasto
    return nuevo_presupuesto

def insertar_gasto_en_db(gasto, nuevo_presupuesto):
    try:
        connection = connect_to_db()
        query = "INSERT INTO gastos (gasto, presupuesto) VALUES (%s, %s);"
        values = (gasto, nuevo_presupuesto)
        
        execute_query(connection, query, values)
        print("Gasto agregado a la base de datos.")
    except Exception as e:
        print(f"Error al agregar el gasto en la base de datos: {e}")
    finally:
        connection.close()

def obtener_gastos_desde_db():
    try:
        connection = connect_to_db()
        query = "SELECT id, gasto, presupuesto FROM gastos;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:
        print(f"Error al obtener los gastos desde la base de datos: {e}")
        return []

presupuesto_inicial = obtener_presupuesto_inicial()
presupuesto_actual = presupuesto_inicial

while True:
    print("Menú:")
    print("1. Agregar gasto")
    print("2. Ver resumen de gastos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        gasto = obtener_gasto()
        if gasto <= presupuesto_actual:
            presupuesto_actual = agregar_gasto(presupuesto_actual, gasto)
            insertar_gasto_en_db(gasto, presupuesto_actual)
        else:
            print("Error: El gasto supera el presupuesto actual.")
    elif opcion == "2":
        gastos_desde_db = obtener_gastos_desde_db()
        print("Resumen de gastos:")
        for gasto_info in gastos_desde_db:
            print(f"ID: {gasto_info[0]}, Gasto: {gasto_info[1]}, Presupuesto Restante: {gasto_info[2]}")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
