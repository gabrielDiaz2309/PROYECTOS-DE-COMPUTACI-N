import math
from fractions import Fraction

# Pedir al usuario que ingrese un número
try:
    n_str = input('Ingresa un número entero positivo: ')
    
    # Convertir la entrada a un objeto Fraction
    n_fraction = Fraction(n_str)

    # Verificar si el número tiene parte fraccionaria
    if n_fraction.denominator != 1 or n_fraction < 0:
        raise ValueError('Ingresa un número entero positivo.')

    # Convertir a entero
    n = int(n_fraction)

    # Calcular el factorial usando la función math.factorial
    factorial = math.factorial(n)

    # Mostrar el resultado
    print(f'El factorial de {n} es {factorial}')

except ValueError as ve:
    # Manejar el error si el usuario ingresa un número con fracción
    print(f'Error: {ve}')
except OverflowError as oe:
    # Manejar el error en caso de desbordamiento
    print(f'Error: {oe}')
except Exception as e:
    # Manejar cualquier otro tipo de excepción
    print(f'Error: {e}')
