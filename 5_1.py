#Denisova Ekaterina katia_kos@mail.ru
#1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

with open('text.txt', 'w') as file:
        input_user = input("Введите текст (для прекращеня ввода введите 'пробел') \n ")
        while input_user:
            file.writelines(f'{input_user} \n')
            input_user = input("Введите текст (для прекращеня ввода введите 'пробел') \n ")
with open('text.txt', 'r') as file:
  for line in file:
      print(line)