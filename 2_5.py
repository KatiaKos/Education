#DenisovaEkaterina katia_kos@mail.ru
#2.5 Реализовать структуру «Рейтинг», представляющую собой
# набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.

my_rating = [7, 5, 3, 3, 2]
u_rating = int(input("Введите чисто в рейтинге: "))
inserted = False
for index, elem in enumerate(my_rating):
    if u_rating > elem:
        my_rating.insert(index, u_rating)
        inserted = True
        break
if not inserted:
    u_rating.append(u_rating)

print (my_rating)


