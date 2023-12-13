import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-50, 51)
x = np.cos(np.pi * 0.1 * n)
y = np.cos(np.pi * 0.9 * n)
z = np.cos(np.pi * 2.1 * n)

plt.subplot(3, 1, 1)
plt.plot(n, x)
plt.title(r'$x[n]=\cos(0.1\pi n)$')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(n, y)
plt.title(r'$y[n]=\cos(0.9\pi n)$')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(n, z)
plt.title(r'$z[n]=\cos(2.1\pi n)$')
plt.grid()

plt.xlabel('n')

plt.show()
