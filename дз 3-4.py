import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = np.linspace(-2, 5, 201)
y = np.linspace(-2, 5, 201)
x != 0
plt.plot(x,(np.exp(x) + x - 1)/ x)
plt.plot(x, x ** 2 - 1)
print(x, y, 10)

plt.plot([-2, 3], [5.8548, 5.8548], color = 'red', linewidth = 0.75, linestyle = '--')
plt.plot([-2, 3], [1.504, 1.504], color = 'red', linewidth = 0.75, linestyle = '--' )
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(-1, 10)
plt.grid(True)
plt.show()