#Denisova Ekaterina katia_kos@mail.ru
#5. Реализовать класс Stationery (канцелярская принадлежность).
#● определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
#● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#● в каждом классе реализовать переопределение метода draw. Для каждого класса
#метод должен выводить уникальное сообщение;
#● создать экземпляры классов и проверить, что выведет описанный метод для каждого
#экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск  отрисовки!")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск  отрисовки ручкой {self.title} !")

class Pencile(Stationery):
    def draw(self):
        print(f"Запуск  отрисовки карандашом {self.title} !")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск  отрисовки маркером {self.title}!")


pen = Pen ('red')
pencil = Pencile('HB')
handle = Handle('Light')
for i in (pen, pencil, handle):
    i.draw()

