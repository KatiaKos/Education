import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



a = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(f'Матрица а = {a} ')
# определитель 5.2
z = np.linalg.det(a)
print(f' Определитель матрицы а ={z}')
 # обратная матрица 5.3
r = np.linalg.inv(a)
print(f'Матрица,обратна а = {r}')
  #Ранг матрицы
print(f'Ранг матрицы а = {np.linalg.matrix_rank(a, 0.0001)}')

  # 5.4
b = np.array([1, 5], float)
c = np.array([2, 8], float)
plt.quiver(b, c, angles='xy', scale_units='xy', scale=1)
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.grid(True)
#plt.show()
print(f'Скалярное произведение векторов b и c = {np.dot(b, c)}')
   # 5.5
d = np.array([1, 5, 0], float)
e = np.array([2, 8, 7], float)
f = np.array([7, 1.5, 3], float)
v = np.cross(d, e)
print (f'Смешанное произведение трех векторов = {np.inner(v, f)}')

w = np.cross(d, f)
print(np.inner(w, e))