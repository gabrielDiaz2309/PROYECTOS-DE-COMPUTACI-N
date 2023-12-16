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

def agregar_venta_en_db(producto, ventas):
    try:
        connection = connect_to_db()
        query = "INSERT INTO ventas (producto, ventas) VALUES (%s, %s);"
        values = (producto, ventas)
        
        execute_query(connection, query, values)
        print("Datos de venta agregados a la base de datos.")
    except Exception as e:
        print(f"Error al agregar los datos de venta en la base de datos: {e}")
    finally:
        connection.close()

def generar_informe_ventas():
    try:
        connection = connect_to_db()
        query = "SELECT producto, ventas FROM ventas;"
        
        cursor = connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:
        print(f"Error al generar el informe de ventas desde la base de datos: {e}")
        return []

def analizar_ventas(resultados):
    total_ventas = sum(venta[1] for venta in resultados)
    promedio_ventas = total_ventas / len(resultados)
    
    print(f"Total de ventas: {total_ventas}")
    print(f"Promedio de ventas por producto: {promedio_ventas}")
    print("Productos con ventas superiores al promedio:")
    
    for producto, ventas in resultados:
        if ventas > promedio_ventas:
            print(f"{producto}: {ventas}")

while True:
    print("Menú:")
    print("1. Agregar datos de venta")
    print("2. Generar informe de ventas")
    print("3. Analizar ventas")
    print("4. Salir")
    
    opciones_validas = ["1", "2", "3", "4"]
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        try:
            producto = input("Ingrese el nombre del producto: ")
            ventas = float(input("Ingrese la cantidad de ventas: "))
            agregar_venta_en_db(producto, ventas)
        except Exception as e:
            print(f"Error: {e}")
    elif opcion == "2":
        informe_ventas = generar_informe_ventas()
        print("Informe de ventas:")
        for venta_info in informe_ventas:
            print(f"Producto: {venta_info[0]}, Ventas: {venta_info[1]}")
    elif opcion == "3":
        informe_ventas = generar_informe_ventas()
        analizar_ventas(informe_ventas)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
