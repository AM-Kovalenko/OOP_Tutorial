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
class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value

    def __delete__(self, instance):
        pass


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        print("вызов __getCoordX")
        return self.__x

    @coordX.setter
    def coordX(self, x):
        print("вызов __setCoordX")
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")
    @coordX.deleter
    def coordX(self):
        print("удаление свойства")
        del self.__x

    # coordX = property(__getCoordX, __setCoordX, __delCoordX)


pt = Point(1, 2)
pt.coordX = 100
x = pt.coordX
print(x)
del pt.coordX
