# Solicitar al usuario que ingrese los lados del triángulo
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

# Inicializar la variable de salida
salida = ""

# Verificar si los lados forman un triángulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Determinar el tipo de triángulo
    if lado1 == lado2 and lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"

    # Concatenar el tipo de triángulo a la variable de salida
    salida += f"El triángulo es de tipo: {tipo_triangulo}\n"

    # Almacenar el resultado en un archivo de texto
    with open('ejercicio6.txt', 'w') as file:
        file.write(f'Tipo de triángulo= {tipo_triangulo}\n')
        file.write(f'Lados del triángulo= {lado1}, {lado2}, {lado3}\n')

    # Conexión a la base de datos PostgreSQL
    import psycopg2

    try:
        conn = psycopg2.connect(
            dbname='ExamenCorto1',
            host='localhost',
            port='5432',
            user='postgres',
            password='gabrielgrdb'
        )

        cursor = conn.cursor()

        query = f"INSERT INTO salida VALUES ('{salida}');"
        cursor.execute(query)

        conn.commit()

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

    finally:
        cursor.close()
        conn.close()

else:
    salida = "Los lados proporcionados no forman un triángulo."

# Mostrar la variable de salida
print(salida)
