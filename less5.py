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