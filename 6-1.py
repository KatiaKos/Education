#Denisova Ekaterina katia_kos@mail.ru
#1. Создать класс TrafficLight (светофор).
#● определить у него один атрибут color (цвет) и метод running (запуск);
#● атрибут реализовать как приватный;
#● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
#зелёный;
#● продолжительность первого состояния (красный) составляет 7 секунд, второго
#(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#● переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#● проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep

class TrafficLight:
    color = ('red','yellow', 'green')
    timeslen = (7, 2, 15)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
             for i in self.color:
                 self.__color = i
                 print(self.__color)
                 sleep(self.timeslen[self.color.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.running()



