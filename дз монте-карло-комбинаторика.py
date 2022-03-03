import numpy as np
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymc3 as pm
from scipy import stats
from math import factorial
import arviz as az
import matplotlib.pyplot as plt

k, n = 5, 6
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1

def num_of_successes(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))


print(a, b, c, d)
print(f'вероятность выпадения орла и решки = {x}')
print(f'количество успехов = {k},  колическтво испытаний = {n}, оценка вероятности = {k/n}')
print(f'Биномиальное распределение = {num_of_successes(n, k)}')

