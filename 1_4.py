
#Denisova Ekaterina katia_kos@mail.ru
#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input("введите целое положительное число:"))
max_N = 0
while n > 0:
    if n % 10 > max_N:
        max_N = n % 10
        if max_N == 9:
            break
    n = n // 10
print("Максимальная цифра в числe",  max_N)
