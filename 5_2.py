#Denisova Ekaterina katia_kos@mail.ru
#2. Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('file 5_2.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        word_count = len(line.split())
        print(f' В {num + 1} строчке - {word_count} слов')
    print(f' Всего {str_count}  строк')