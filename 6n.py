import numpy as np
import pandas
# import pylab
import scipy.stats as stats
from scipy.stats import norm

print(f'1.Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков.')
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

print(np.corrcoef(ks, zp))  # коэфф корреляции R

# cov=m(xy)-m(x)m(y)    m-mat ojid
print(f'ковариация = {np.mean(zp * ks) - np.mean(zp) * np.mean(ks)}')
print(np.cov(ks, zp, ddof=1))  # смещенная ковариация

print(np.std(zp))  # не смещенное мат ожидание  ddof=0
print(np.std(ks))
print(f' критерий Пирсона = {np.cov(ks, zp, ddof=1) / (np.std(zp, ddof=1) * np.std(ks, ddof=1))}')

print(f"2.Найдите дов.интервал для мат.ожидания с надежностью 0.95")
# Найдите дов.интервал для мат.ожидания с надежностью 0.95.
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
print(f'iq = {iq}')
y = 0.95
t = 2.262
s = np.std(iq, ddof=1)
m = iq.mean()  # 118.1

k = len(iq) - 1  # = print(iq.shape[0]) #9
print(f'k = n-1 = {len(iq) - 1}')
print(f'оценка сред.кв.откл.(s) = {s}')  # оценка среднего квад.откл
print(f'среднее (m) = {m}')  # среднее
print(f'дов.интервал = {m - (t * s) / np.sqrt(k), m + (t * s) / np.sqrt(k)}')

print(f'3.Известно, что рост футболистов в сборной распределен нормально'
      'с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,'
      'среднее выборочное составляет 174.2. Найдите доверительный интервал для математического'
      'ожидания с надежностью 0.95')
k1 = 27
m1 = 174.2
s1 = np.sqrt(25)
y1 = 0.95
t1 = 1.96

print(f'дов.интервал = {m1 - (t1 * s1) / np.sqrt(k1), m1 + (t1 * s1) / np.sqrt(k1)}')

# notes
# norm.ppf(0.975)  # табл обратная по квантилю   z
# norm.cdf(1.96)   №табл норм распред
