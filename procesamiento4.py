import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-3, 8)
x = 0.55**(n + 3)
h = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y = np.convolve(x, h, mode='full')

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt='b-', use_line_collection=True)
plt.title('Original Signal')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(3, 1, 2)
plt.stem(range(len(h)), h, basefmt='r-', use_line_collection=True)
plt.title('Impulse Response / Second Signal')
plt.xlabel('n')
plt.ylabel('h[n]')

plt.subplot(3, 1, 3)
plt.stem(range(len(y)), y, basefmt='g-', use_line_collection=True)
plt.title('Resultant Convolution')
plt.xlabel('n')
plt.ylabel('y[n]')

plt.tight_layout()
plt.show()
