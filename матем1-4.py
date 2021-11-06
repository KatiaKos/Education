#%matplotlib_inline
import numpy as np
import matplotlib.pyplot as plt
from math import cos
x = np.linspace(-1, 1, 10)

plt.plot(x, x, marker='o')    #x, cos(x),'b--')
def f(x):
    k = 1
    return np.cos(x * k)
diap = np.linspace(-5, 6, 68)
y = f(diap)
plt.plot( diap, y, marker = 'x')
plt.show()

