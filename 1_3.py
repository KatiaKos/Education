###Denisova Ekaterina katia_kos@mail.ru
#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#n = input("введите  простое число:")
#a = n + n
#b = n + n + n

#print (a)
#print(b)
#c = int(a + b + n)
#print (c)
#print(int(n + a + b))

n = int(input("Введите число n: "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)

