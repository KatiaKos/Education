# Denisova Ekaterina katia_kos@mail.ru
# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка
# в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с
# параметрами.
import sys
if  len(sys.argv) < 4:
   print( f"Введите необхожимые данные")
else:
    time = float(sys.argv[1])
    salary = float(sys.argv[2])
    bonus = float(sys.argv[3])
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
