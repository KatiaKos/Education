# Denisova Ekaterina katia_kos@Mail.ru
# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def func(n, s, y, c, e, p):
    print(f'{n} {s} {y} {c} {e} {p}')


n = input("name: ")
s = input('surname: ')
y = input('year: ')
c = input('city: ')
e = input('email: ')
p = input('phone number: ')
func(n, s, y, c, e, p)