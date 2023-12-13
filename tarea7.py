import psycopg2
from datetime import datetime

# Función para conectarse a la base de datos PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        dbname='Ejercicio',
        host='localhost',
        port='5432',
        user='postgres',
        password='gabrielgrdb'
    )
    return conn

# Función para agregar venta en la base de datos
def agregar_venta_en_db():
    conn = connect_to_db()

    try:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto en: Q "))
        descuento = float(input("Ingrese el porcentaje de descuento (0 si no hay oferta): "))

        precio_oferta = precio - (precio * (descuento / 100))
        iva = precio * 0.12
        precio_sin_iva = precio - iva
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with conn.cursor() as cursor:
            ins_query = "INSERT INTO productos (nombre, precio, precio_oferta, fecha) VALUES (%s, %s, %s, %s)"
            cursor.execute(ins_query, (nombre_producto, precio, precio_oferta, fecha_actual))

        conn.commit()
        print("Datos de venta agregados a la base de datos.")
        print(f"El precio sin IVA es de Q{precio_sin_iva:.2f}, por lo que el IVA es de Q{iva:.2f}")
    except Exception as e:
        print(f"Error durante la conexión a la DB, consulte sobre el error: {str(e)}")
    finally:
        conn.close()

# Función para mostrar historial de la base de datos
def mostrar_historial():
    conn = connect_to_db()

    try:
        with conn.cursor() as cursor:
            consulta = 'SELECT * FROM productos;'
            cursor.execute(consulta)
            rows = cursor.fetchall()

            print('%-4s %-20s %-10s %-15s %-20s' % ('ID', 'Nombre', 'Precio', 'Precio Oferta', 'Fecha'))
            print('------------------------------------------------------------')
            for row in rows:
                # Verificar que los valores no sean None antes de realizar operaciones
                id_producto = row[0] if row[0] is not None else 0
                nombre = row[1] if row[1] is not None else ''
                precio = row[2] if row[2] is not None else 0
                precio_oferta = row[3] if row[3] is not None else 0
                fecha = row[4] if row[4] is not None else ''

                print('%-4d %-20s Q%-9.2f Q%-14.2f %-20s' % (id_producto, nombre, precio, precio_oferta, fecha))
    except Exception as e:
        print(f"Error durante la conexión a la DB, consulte sobre el error: {str(e)}")
    finally:
        conn.close()
# Menú interactivo
while True:
    print("Menú:")
    print("1. Agregar datos de venta")
    print("2. Mostrar historial")
    print("3. Salir")

    opciones_validas = ["1", "2", "3"]
    opcion = input("Seleccione una opción: ")

    if opcion in opciones_validas:
        if opcion == "1":
            try:
                agregar_venta_en_db()
            except Exception as e:
                print(f"Error: {str(e)}")
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
