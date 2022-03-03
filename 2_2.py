#Denisova Ekaterina katia_kos@mail.ru
#Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём
# месте. Для заполнения списка элементов нужно использовать
# функцию input()

a = input("введите несколько чисел без пробела")
my_list = list(a)
#my_list = len(my_list)
i = 0

for i in range(0,len(my_list) -1,2):
    my_list[i],my_list[i+1] = my_list[i+1], my_list[i]


print(my_list)


#list = [1, 2, 3, 4, 5]
#print((list[1]), (list[0]), (list[3]), (list[2]), (list[4]))





