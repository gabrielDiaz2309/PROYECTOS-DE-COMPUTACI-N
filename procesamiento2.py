import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-1000, 1001)
x = np.exp(1j * 2 * np.pi * 0.01 * n)
plt.plot(n, np.real(x))

y = np.exp(1j * 2 * np.pi * 2.01 * n)
plt.plot(n, np.real(y), 'r')

plt.show()
