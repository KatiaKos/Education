#Denisova Ekaterina katia_kos@mail.ru
#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.
my_dict = {'One' : 'Один', 'Two' : "Два", "Three" : "Три", "Four" : "Четыре"}
with open('text 5_4.txt') as file, open("newfile5_4.txt","w") as new_file:
    lines = file.readlines()
    for line in lines:
        info = line.split()
        number = my_dict.get(info[0])
        new_file.write(f'{line.replace(info[0], number)}')
