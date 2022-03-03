import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0, 2 * np.pi, 100)

r = np.sqrt(0.6)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)
fig, ax = plt.subplots(1)
ax.plot(x1, x2)
ax.set_aspect(1)

x = np.linspace(-10, 10, 200)
y1 = np.sqrt(1 - (x**2)/16)
y2 = -(np.sqrt(1 - (x**2)/16))

plt.ylim(-10, 5, 10, 5)
plt.xlim(-6, 6)
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)  #сетка
plt.show()