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

#Провести дисперсионный анализ для определения того, есть ли различия
#среднего роста среди взрослых футболистов, хоккеистов и штангистов.
#Даны значения роста в трех группах случайно выбранных спортсменов:
#Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
#Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
#Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

x = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
z = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

n1= len(x)
print('Всего футболистов = ', n1)
n2 = len(y)
print('Всего хоккеистов = ', n2)
n3= len(z)
print('Всего штангистов = ', n3)
n = n1 + n2 + n3
print('Всего спортсменов = ', n)
k = 3 # всего групп исследования
n1_mean = np.mean(x)
print('Средний рост футболистов = ',n1_mean)
n2_mean = np.mean(y)
print('Средний рост хоккеистов = ',n2_mean)
n3_mean = np.mean(z)
print('Средний рост штангистов = ', n3_mean)

n_all = np.concatenate([x, y, z])
#print(n_all)
n_mean = np.mean(n_all) #среднее значение роста спортсменов
print(n_mean)

s2=np.sum((n_all - n_mean)**2)
print('S^2 =', s2) #сумма квадратов отклонений наблюдений от общего среднего
s2_f= ((n1_mean - n_mean)**2) * n1 + ((n2_mean - n_mean)**2) * n2 + ((n3_mean - n_mean)**2) * n3
print('S^2 F=', s2_f)  #сумма квадратов отклонений средних групповых значений от общего среднего
s2_residual = np.sum((x - n1_mean)**2) + np.sum((y - n2_mean)**2) + np.sum((z -n3_mean)**2)
print('остаточная сумма квадратов отклонений',s2_residual) #остаточная сумма квадратов отклонений

#print(s2_f + s2_residual)

sigma2_general = s2 / (n - 1)
print('общая дисперсия =',sigma2_general) #общая дисперсия
sigma2_f = s2_f / (k - 1)
print('факторная дисперсия =', sigma2_f) #факторная дисперсия
sigma2_residual = s2_residual / (n - k)
print('остаточная дисперсия=', sigma2_residual) #остаточная дисперсия

F_h = sigma2_f / sigma2_residual
print('Критерий Фишера=', "%.2f" % F_h) #!!!
a = 0.05
d_f_critic = k - 1 #степень свободы числителя
d_f_intern = n - k #степень свободы знаменателя
print(f'Степени свободы = {d_f_critic} / {d_f_intern}')
F_critic = 3.3852
print(f'Критерий Фишера крит. =', F_critic)
print(f'Так как F_h({"%.2f" % F_h}) > F_critic({"%.2f" % F_critic}) --  гипотеза Н0 отвергнула.\n  Различия роста в группах статистически значимы')

