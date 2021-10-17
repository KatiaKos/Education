#Denisova Ekaterina katia_kos@mail.ru
#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь
#определенное название. К типам одежды в этом проекте относятся пальто и
#костюм. У этих типов одежды существуют параметры: размер (для пальто) и
#рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
#для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
#методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные
#на этом уроке знания: реализовать абстрактные классы для основных классов
#проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
          pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
       return 2 * self.h + 0.3

    def sum_consumption(self, list_suits):
           a = 0
           for suit in list_suits:
                a += suit.consumption
           return a

coat = Coat(50)
costume = Suit(1.96)
costume_2 = Suit(1.24)
costum_3 = Suit(1.76)
costum_4 = Suit(2.10)
list_costumes = [costume, costume_2, costum_3, costum_4]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_consumption(list_costumes))




