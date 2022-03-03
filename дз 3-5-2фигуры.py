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
#Z1 = X**2 + Y**2
Z = ((X**2)/5 )+ ((Y**2)/15)
Z3 = np.sqrt(X**2 + Y**2)
Z4 = - np.sqrt( X**2 + Y**2) #конус с сечением окружности
#ax.plot_wireframe(X, Y, Z1)
ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z3)
ax.plot_wireframe(X, Y, Z4)
ax.scatter(0, 0, 0, 'z', 50, 'red') #график точки в пространстве
show( )