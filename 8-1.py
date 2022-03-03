#Denisova Ekaterina katia_kos@mail.ru

#1. Реализовать класс «Дата», функция-конструктор которого должна принимать
#дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать  их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_data = []

        for i in d_m_y.split():
            if i != "-" : my_data.append(i)
        return int(my_data[0]), int(my_data[1]), int( my_data[2])

    @staticmethod
    def valid( day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <=12:
                if 2021 >= year>= 0:
                    return f"All right"
                else:
                    return f'Error year'
            else:
                return f'error month'
        else:
            return f'error day'
    def __str__(self):
        return f"Today is {Data.extract(self.d_m_y)}"

today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2021))
print(Data.extract('11 - 11 - 2011'))
print(today.extract("11 - 11 - 2020"))
print(Data.valid(1, 11, 2000))

