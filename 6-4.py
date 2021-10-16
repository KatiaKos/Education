#Denisova Ekaterina katia_kos@mail.ru
#4. Реализуйте базовый класс Car.
#● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
#● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#● добавьте в базовый класс метод show_speed, который должен показывать текущую
#скорость автомобиля;
#● для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('GO!')

    def stop(self):
        print("STOP!")

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
          super().show_speed()
          if self.speed > 60:
              print("Reduce your speed!")

class SportCar(Car):
     pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Reduce your speed!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(90,"Green", "Town")
sport = SportCar(120, "Red", "Sport")
work = WorkCar(41, 'Yellow', "Work")
police = PoliceCar(100,'blue','Police')

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn('Left')
