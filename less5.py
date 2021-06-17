# Статические методы и свойства объектов
"""
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"{self.name} - {self.email}")

    @classmethod
    def get_info_class(cls, data):  # обязательный аргумент cls - класс
        name, email = data  # разложили список
        return cls(name, email)  # создание объекта

    @staticmethod
    def get_info_static(self):
        print(f"{self.name} - {self.email}")



user_list = ["Admin2", "test@test.com"]
user = User("Admin", "admin@test.com")
user.get_info()
user = User.get_info_class(user_list)
user.get_info()
user.get_info_static(user)

"""

"""
class Point():
    __count = 0  # статическое свойство внутри класса (приватное )
    __instance = None

    # перегрузка метода new(выполняется перед тем как создать экземпляр класса Point)
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)    # создаем экземпляр
        else:
            print('экземпляр класса Point уже создан!')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x  # при этом в каждом экземпляре будет создаваться локальное свойства
        self.coordY = y

    @staticmethod
    def get_count():
        return Point.__count


pt = Point()
pt2 = Point()
pt3 = Point()
print(id(pt), id(pt2), id(pt3),)
"""

'''
1. Объявите класс Rectangle (прямоугольник), в котором имеется статический метод, вычисляющий площадь прямоугольника. 
Этот метод принимает два параметра (ширину и длину), вызывается в конструкторе для вычисления площади конкретного 
прямоугольника и результат присваивается локальному свойству создаваемого экземпляра класса.
'''

"""
class Rectangle:
    __res = 0

    def __init__(self, a, b):
        self.res = Rectangle.getArea(a, b)
        print(self.__res)

    @staticmethod
    def getArea(a, b):
        return a * b


ex = Rectangle(2, 3)
ex2 = Rectangle(2, 3)

print(id(ex.res), id(ex2.res))"""

"""
2. Создайте класс Dog (собака), в каждом его экземпляре создавайте несколько локальных свойств 
(например: имя, возраст, порода) и сделайте так, чтобы можно было создавать не более пяти экземпляров этого класса.
"""


class Dog:
    __count = 0

    def __new__(cls, *args, **kwargs):
        print(Dog.__count)
        if cls.__count < 5:
            instance = super(Dog, cls).__new__(cls)  # ???????
            cls.__count += 1
            return instance
        else:
            print(f"max quality ex: {Dog.__count}")

    def __init__(self, name="name", age="age", type="type"):
        self.name = name
        self.age = age
        self.type = type


d11 = Dog()
d12 = Dog("1", "2", "3")
d13 = Dog()
d14 = Dog()
d15 = Dog()
d16 = Dog()
print( id(d11), id(d12), id(d13), id(d14), id(d15), id(d16), sep="\n")
