# 1. Создайте базовый класс «Стол» и дочерние: «Прямоугольные столы» и «Круглые столы».
# Через конструктор базового класса передавайте размер поверхности стола: для прямоугольного – ширина и длина,
# для круглого – радиус. В дочерних классах реализуйте метод вычисления площади поверхности стола.
"""
class Table:
    def __init__(self, a, b=None):
        if b is None:
            self.radius = a
        else:
            self.height = a
            self.weight = b


class RectTable(Table):
    def calcArea(self):
        area = self.height * self.weight
        return print(f"area of rectangle: {area}")


class CircleTable(Table):
    def calcArea(self):
        area = 3.14 * self.radius ** 2
        return print(f"area of circle: {area}")


rt = RectTable(3, 3)
rt.calcArea()
ct = CircleTable(1.5)
ct.calcArea()
"""
"""
2. Создайте класс Animal (животное) и разные производные от него подклассы: Fox, Bird, Cat, Dog и т.п. 
Реализуйте у них общий метод say(), который бы возвращал звук, издаваемый этим животным. 
Создайте кортеж из нескольких этих экземпляров классов, переберите их в цикле и выведите в консоль их звуки 
(вызовите метод say()).
"""


class Animal:
    pass


class Dog(Animal):
    def say(self):
        print("gaf")


class Cat(Animal):
    def say(self):
        print("miaw")

c1 = Cat()
d1 = Dog()
tpl = c1, d1

for i in tpl:
    i.say()

