import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango de tiempo
t = np.arange(-0.04, 0.041, 0.001)

# Guardamos la función en x
x = 20 * np.exp(1j * (80 * np.pi * t - 0.4 * np.pi))

# Creamos la figura
fig = plt.figure()

# Posicionamos la primera imagen en 3D
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot3D(t, np.real(x), np.imag(x))
ax1.set_title('20*e^{j*(80*pi*t-0.4*pi)}')
ax1.set_xlabel('Tiempo, s')
ax1.set_ylabel('Real')
ax1.set_zlabel('Imag')

# Posicionamos la segunda imagen
ax2 = fig.add_subplot(122)
ax2.plot(t, np.real(x), 'b', label='Componente Real')
ax2.plot(t, np.imag(x), 'r', label='Componente Imaginario')
ax2.grid()
ax2.set_title('Rojo - Componente Imaginario, Azul - Componente Real de la Exponencial')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Amplitud')
ax2.legend()

# Mostramos las gráficas
plt.show()
