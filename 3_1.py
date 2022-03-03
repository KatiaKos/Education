#Denisova Ekaterina katia_kos@Mail.ru
#1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
arg_1 = int(input("Введите число  "))
arg_2 = int(input(f" {arg_1} разделить на   "))

def func_devision(arg_1, arg_2):
    if arg_2 == 0:
          print = int(input('разделить на нуль нельзя. Введите другое число :'))
    else:
        return  arg_1/arg_2
print(func_devision(arg_1, arg_2))
