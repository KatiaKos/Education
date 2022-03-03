import numpy as np
import matplotlib.pyplot as plt

#я знаю, что все здесь не верно, обьясните , поэалуйста, эту тему на лекции!
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) ** 2 + np.cos(x) ** 2
y1 = x * 30

plt.polar(x, y1, linewidth = 0.75, color = 'red' )
#y = np.sin(x) ** 2 + np.cos(x) ** 2
plt.polar(x, y, 'g')

plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 2)
plt.grid(True)  #сетка
plt.show()