#Denisova Ekaterina katia_kos@Mail.ru
#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских
# букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#7. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(text):
    s = text[0].upper() + text[1:].lower()    # s = text[0].capitalize() + text[1:].lower()
    return s

input_user = input ('введите текст: ')
for s in input_user.split(' '):
  print (f'{int_func(s) }', end=' ')
