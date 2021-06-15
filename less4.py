# обекты-асвойства (property)
"""
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def __getCoordX(self):
        print("вызов __getCoordX")
        return self.__x

    def __setCoordX(self, x):
        print("вызов __setCoordX")
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")
    def __delCoordX(self):
        print("удаление свойства")
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __delCoordX)


pt = Point(1, 2)
pt.coordX = 100
x = pt.coordX
print(x)
del pt.coordX
"""

"""


class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # функция проветки воодимой переменной
    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property                           # декоратор свойство
    def coordX(self):
        print("вызов __getCoordX")
        return self.__x

    @coordX.setter                       # декоратор
    def coordX(self, x):
        print("вызов __setCoordX")
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    @coordX.deleter                      # декоратор
    def coordX(self):
        print("удаление свойства")
        del self.__x

    # coordX = property(__getCoordX, __setCoordX, __delCoordX)      # объект-свойство


pt = Point(1, 2)
pt.coordX = 100
x = pt.coordX
print(x)
del pt.coordX
"""

"""
# Клас-дескриптор
class CoordValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value




class Point:
    coordX = CoordValue("coordX")  # создание экземпляра.  coordX, coordY - дескрипторы
    coordY = CoordValue("coordY")

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt = Point(1, 1)
pt2 = Point(2, 2)
print(pt.coordX, pt.coordY)
pt.coordX = 5

print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)

"""

"""
1. Объявите класс Calendar для хранения даты: день, месяц, год.
 Определите свойства для записи и считывания этой информации из этого класса. 
 (Дополнение: используя __slots__ разрешите использовать только строго определенные 
 локальные свойства в экземплярах класса).
"""

"""
class Calendar:
    __slots__ = ["__day", "__month", "__year"]

    def __init__(self, day=0, month=0, year=0):
        print("init")
        self.__day = day
        self.__month = month
        self.__year = year

    def getDate(self):
        print("getDate")
        return self.__day, self.__month, self.__year

    def setDate(self, day, month, year):
        print("setDate ")
        self.__day = day
        self.__month = month
        self.__year = year


c = Calendar()
x = c._Calendar__day = 11
print(c.getDate())
"""

"""

# класс-дескриптор(зачем?? для "гибкости??")
class DateValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value



class Calendar:

    day = DateValue("day")
    month = DateValue("month")
    year = DateValue("year")

    def __init__(self, day=0, month=0, year=0):
        print("init")
        self.day = day
        self.month = month
        self.year = year




c = Calendar()
print(c.day, c.month, c.year)

c.day = 12
c.month = 2
c.year = 1988
print(c.day, c.month, c.year)

"""





"""
2. Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек.
 Создайте дескрипторы для записи и считывания этих значений в классе 
 (атрибуты с данными координат должны быть приватными).
"""

"""
class ValueRectangle:
    def __set__(self, instance, value):
        self.__value = value


    def __get__(self, instance, owner):
        return self.__value

class Rectangle:

    pt1 = ValueRectangle()
    pt2 = ValueRectangle()



    def __init__(self, pt1=[0, 0], pt2=[0, 0]):
       self.__pt1 = pt1
       self.__pt2 = pt2


r = Rectangle()
r.pt1 = [1,11,12]
print(r.pt1)
"""


