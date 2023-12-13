import numpy as np
import matplotlib.pyplot as plt

# Generar señal senoidal
fs = 1000  # frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # vector de tiempo
f = 100  # frecuencia de la señal
x = np.sin(2 * np.pi * f * t)  # Definimos la variable x para la señal senoidal

# Aplicar Transformada de Fourier
xf = np.fft.fft(x)

# Generar filtro pasa-bajo
n = len(x)
fcutoff = 50  # frecuencia de corte
h = np.ones(n)  # vector de unos
h[int(n * fcutoff / fs) + 1:] = 0  # aplicar filtro pasa-bajo

# Aplicar filtro a la señal en el dominio de la frecuencia
xf_filtered = xf * h

# Convertir señal filtrada a dominio del tiempo
x_filtered = np.fft.ifft(xf_filtered)

# Graficar señal original y señal filtrada
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Señal original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.subplot(2, 1, 2)
plt.plot(t, np.real(x_filtered))
plt.title('Señal filtrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()
