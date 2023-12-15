import math
import psycopg2

def calcular_y_guardar_areas():
    # Menú de selección
    print('Seleccione la figura geométrica:')
    print('1. Círculo')
    print('2. Triángulo')
    print('3. Cuadrado')
    print('4. Rectángulo')

    opcion = int(input('Ingrese el número de la opción deseada: '))

    # Definir las variables de área y figura
    area = 0
    figura = ''

    if opcion == 1:
        # Área de un círculo
        radio = float(input('Ingrese el radio del círculo: '))
        area = math.pi * radio ** 2
        figura = 'Círculo'
    elif opcion == 2:
        # Área de un triángulo
        base = float(input('Ingrese la base del triángulo: '))
        altura = float(input('Ingrese la altura del triángulo: '))
        area = 0.5 * base * altura
        figura = 'Triángulo'
    elif opcion == 3:
        # Área de un cuadrado
        lado = float(input('Ingrese el lado del cuadrado: '))
        area = lado ** 2
        figura = 'Cuadrado'
    elif opcion == 4:
        # Área de un rectángulo
        base = float(input('Ingrese la base del rectángulo: '))
        altura = float(input('Ingrese la altura del rectángulo: '))
        area = base * altura
        figura = 'Rectángulo'
    else:
        print('Opción no válida.')
        return None

    # Mostrar el resultado
    print(f'El área del {figura} es: {area:.4f}')

    # Crear la cadena de texto
    cadena_resultado = f'Figura: {figura}, Área: {area:.4f}'

    # Guardar el resultado en un archivo de texto
    guardar_en_archivo(cadena_resultado)

def guardar_en_archivo(cadena_resultado):
    # Abrir el archivo en modo de escritura
    with open('ejercicio12.txt', 'a') as archivo:
        # Escribir el resultado en el archivo
        archivo.write(f'{cadena_resultado}\n')

    # Conexión a la base de datos PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname='ExamenCorto1',
            host='localhost',
            port='5432',
            user='postgres',
            password='gabrielgrdb'
        )

        # Crear un cursor
        cursor = conn.cursor()

        # Ejecutar la consulta SQL
        query = f"INSERT INTO salida VALUES ('{cadena_resultado}')"
        cursor.execute(query)

        # Confirmar la transacción
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        print('Resultado guardado en "resultados.txt" y en la base de datos.')
    except Exception as e:
        print(f'Error al guardar en la base de datos: {e}')

# Ejecutar la función principal
calcular_y_guardar_areas()
