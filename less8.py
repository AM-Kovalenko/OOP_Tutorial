"""
Создайте дочерний класс Motherboard (материнская плата), которая наследуется от классов:
CPU (процессор), GPU (графич. сопроцессор), Memory (память).
В свою очередь CPU наследуется от классов: AMD и Intell, GPU от классов NVidia, GeForce.

Создайте экземпляр класса Motherboard и наполните ее конкретным содержимым
(локальным свойствам этого объекта присвойте определенные значения).
Определите вспомогательные методы в базовых классах и выведите итоговую информацию в консоль с помощью метода showInfo()
класса Motherboard.
"""

"""class AMD:
    pass


class Intell:
    pass


class NVidia:
    pass


class GeForce:
    pass


class CPU(AMD, Intell):
    def __init__(self):
        super().__init__()


class GPU(NVidia, GeForce):
    def __init__(self):
        super().__init__()


class Memory:
    def __init__(self):
        super().__init__()


class Motherboard(Memory, CPU, GPU):
    def __init__(self, name, memory, type_GPU):
        self.name = name
        self.memory = memory
        self.type_GPU = type_GPU

    def showInfo(self):
        print(f"характеристики материнки: {self.name}, память:{self.memory}, тип GPU:{self.type_GPU} ")


m = Motherboard('aaa',100,"asaa")
m.showInfo()
m.type_GPU = 123
m.showInfo()
print(Motherboard.__mro__)"""

"""
В этой задаче у нас будет один родительский класс Transport и три дочерних класса (Car, Boat, Plane).

В классе Transport должны быть реализованы:

метод __init__, который создает атрибуты brand, max_speed и kind. 
Значения атрибутов brand, max_speed, kind поступают при вызове метода __init__. 
При этом значение kind не является обязательным и по умолчанию имеет значение None;
метод __str__, который будет возвращать строку формата: "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".

В классе Car должны быть реализованы:
метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue. 
Все значения этих атрибутов передаются при вызове класса Car. 
Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport, 
при этом атрибуту kind передайте значение "Car";
свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина на <gasoline_residue> км";
свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value, увеличивает уровень топлива gasoline_residue 
на переданное значение и затем вывести фразу 'Объем топлива увеличен на <value> л и составляет <gasoline_residue>'. Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.

В классе Boat должны быть реализованы:
метод __init__, создающий у экземпляра атрибуты brand, max_speed, kind, owners_name. 
Все значения этих атрибутов передаются при вызове класса Boat. Внутри инициализации делегируйте создание атрибутов 
brand, max_speed, kind родительскому классу Transport, при этом атрибуту kind передайте значение "Boat";
метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.

В классе Plane должны быть реализованы:
метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity. 
Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport, 
при этом атрибуту kind передайте значение "Plane";
метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
"""


class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, mileage, gasoline_residue):
        self.brand = super().brand
        self.max_speed = super().max_speed

        super().self.kind = "Car"
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue


class Boat(Transport):
    pass


class Plane(Transport):
    pass


t=Transport("suzuki",100)
print(t)

c = Car(1000000, 56)
print(c)