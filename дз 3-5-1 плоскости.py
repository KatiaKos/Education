import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()         #отрисовка трехмернго пространства х-у-z
ax = Axes3D(fig)
auto_add_to_figure=False
fig.add_axes(ax)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 2 * X - 5 * Y #плоскость 1
Z2 = 2 * X - 5 * Y + 7 #плоскость 2
ax.plot_surface(X, Y, Z, rstride=2, cstride=1, cmap='gnuplot')
ax.plot_wireframe(X, Y, Z2)
ax.scatter(0, 0, 0, 'z', 50, 'red') #график точки в пространстве
show( )