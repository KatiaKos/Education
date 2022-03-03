#Denisova Ekaterina katia_kos@mail.ru
#2.4 Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

user = input('Введите несколько слов через пробел: ')
user_list = user.split( )
#u_list = list(user_list)
for num, word in enumerate(user_list):

    print(num, word[:10])





