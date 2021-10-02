#Denisova Ekaterina katia_kos@Mail.ru
#1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
user_1 = int(input("Введите число"))
user_2 = int(input(f"Pазделить {user_1} на :  "))
if user_2 == 0:
    print = int(input('разделить на нуль нельзя. Введите другое число :')
def func_devision(arg_1, arg_2):
   result = arg_1/arg_2
   return result
print(func_devision(user_1, user_2))
