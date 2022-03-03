import numpy as np
import matplotlib.pyplot as plt

#3 polaric
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) ** 2 + np.cos(x) ** 2
plt.polar(x, y, 'g')

plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 2)
plt.grid(True)  #сетка
plt.show()