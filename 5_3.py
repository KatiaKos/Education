#Denisova Ekaterina katia_kos@mail.ru
#3. Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('file 5_3.txt', 'r') as file:
    lines = file.readlines()
    surname = {}  # словарь
    sum_salary = 0
    for line in lines:
        info = line.split()
        surname.update({info[0]: float(info[1])})
        sum_salary += float(info[1])
middle_sal = sum_salary / len(surname)
print (f' Middle_salary:{middle_sal}')

for keys, values in surname.items():
  if values < 20000:
      print(f'{keys}: {values}')




