#Denisova Ekaterina katia_kos@mail.ru
#5. Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file5_5.txt', 'w') as file:
    file.write(input(f"введите ряд чисел через пробел: "))

with open('file5_5.txt') as file:
        info = file.read().split()
        sum = 0
        for num in info:
            sum += int(num)

print(sum)


