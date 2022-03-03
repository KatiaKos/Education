#Denisova Ekaterina katia_kos@Mail.ru
#3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func(num_1,num_2, num_3):
    sum_nums = num_1 + num_2 + num_3
    return sum_nums - min(num_1, num_2, num_3)


num_1 = int(input("первое число: "))
num_2 = int(input("второе число: "))
num_3 = int(input("третье число: "))
my_func(num_1, num_2, num_3)
print(f'Сумма наибольших введенных чисел равна {my_func(num_1, num_2, num_3)}')