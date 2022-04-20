import inline as inline
import intercept as intercept
import matplotlib
import np as np
import numpy as np
import pandas
import pandas as pd
import scipy.stats as stats
from numpy import ndarray
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного
# скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])  # x   зарплата
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])  # y  скрин балл
n = len(x)
print('n = ', n)

b1 = (np.mean(x * y) - np.mean(x) * np.mean(y) )/ (np.mean(x**2) - (np.mean(x)**2))
print('b1 =', b1)
b2 = (n * (np.sum(y*x)) - (np.sum(x) * np.sum(y))) / (n * (np.sum(x**2)) - ((np.sum(x)**2)))
print('b2 =', b2)

a = np.mean(y) - (b2 * np.mean(x))
print('a =', a)

y_hat = a + (b2 * x)
print('y_hat = ', y_hat)
print('y = ',y)

mse = ((y - y_hat)**2).sum()/n #среднеквадратичная ошибка
print('mse =' ,mse)

plt.scatter(x, y)
plt.plot(x, a + b2 * x, color = 'red')
plt.show()

x1 = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]).reshape((-1, 1))  # x   зарплата
y1 = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])  # y  скрин балл

print('x = ',x1)
print('y = ',y1)

model = LinearRegression().fit(x1, y1)
r_sq = model.score(x1, y1)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
new_model = LinearRegression().fit(x1, y1.reshape((-1, 1)))
print('intercept:', new_model.intercept_)

print('slope:', new_model.coef_)