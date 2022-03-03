import numpy as np
import scipy.linalg

# 6.1
from matplotlib import pyplot as plt

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
print(np.linalg.solve(A, B))

# 6.2 !!!
i = np.array([[1, 3, 8, 2, 11], [2, -4, -5, -5, 4], [-1, 0, 2, 0, -7]])
h = np.array([[1, 7, 12, 7, 15]])
# print(np.linalg.det(i))
# print(np.linalg.matrix_rank(i, 0.0001))
# print(np.linalg.lstsq(i, h))

# 6.3
C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = np.array([12, 2, 1])
E = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

if np.linalg.det(C) == 0.0:
    print('Определитель матрицы = 0,\n Линейная система не имеет решений.\n  Данная матрица была изменена.')
    F = C + E
    print(f' Результат сложения с новой матрицей {np.linalg.solve(F, D)}')
else:
    print(np.linalg.solve(C, D))
# 6.4
M = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(M)
print(P)
print(L)
print(U)
print(np.dot(P, M) - np.dot(L, U))

# 6.5!!!
G = np.array([[1, 8], [2, -5], [-1, 2]])
J = np.array([[1, 12]])
# O = np.concatenate((G, J.T), axis=0)
print(G)
print(np.linalg.lstsq(G, J))
print(f'Норма решения = {np.linalg.norm(G)}')
print(np.linalg.matrix_rank(G, 0.0001), np.linalg.matrix_rank(O, 0.0001))

# 6.6!!!
x = np.linspace(-1, 5, 201)
A1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B1 = np.array([2, 5, 11])
A2 =np.linalg.inv(A1)
plt.plot(x, B1 * A2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
print(np.linalg.lstsq(A2, B1))
print(np.linalg.det(A1))