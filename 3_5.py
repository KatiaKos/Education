#Denisova Ekaterina katia_kos@Mail.ru
#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def func(nums_l, stop):
    nums_list = nums_l.split(' ')
    sum_list = 0
    for i in nums_list:
       if i == stop:
           break
       sum_list += int(i)

    return sum_list


stopper = '#'
finished = False
s = 0
while not finished:
    nums = input(' введите несколько чисел через пробел:  ')
    s += func(nums, stopper)
    finished = stopper in nums
    print(f'Сумма : {s}')