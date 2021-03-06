#Denisova Ekaterina katia_kos@mail.ru
#7. Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.
import json
companies = {}
count, sum = 0, 0
with open('file5_7.txt', 'r')as file:
    lines = file.readlines()
    for line in lines:
        info = line.split()
        profit = float(info[2]) - float(info[3])
        companies.update({info[0] : profit})
        if profit > 0:
            count += 1
            sum += profit

average_profit = sum /count
result = [companies, {'average_profit' : average_profit}]

with open('file5_7.json', 'w') as file:
    json.dump(result, file)

