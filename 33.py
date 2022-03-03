import statistics
import math
import numpy
import array

import numpy as np
from numpy import std, var

z = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
print(z)
print(f'число объектов выборки m = {len(z)}')
m = len(z)

l = sorted(z)
print(f'список по порядку {l}')
print(f'среднее арифметическое N = {sum(z) / m}')
N = sum(l) / len(z)

S = (np.sum(np.array(z)-N))**2
print(S)
print(f'cреднее квадратичное отклонение {(S) / m**0.5}')   # 30.823
print(f'Cмещенная дисперсия {S/m}') # 950.11
print(f'Несмещенная дисперсия  {S/ (m-1) }') #1000.115


