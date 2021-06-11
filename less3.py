class Point:
    def __init__(self, x, y):
        self.__x = x
        self.y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.y = y
        else:
            print("not int or float")

    def getCoords(self):
        return self.__x, self.y


pt = Point(1, 2)
pt.setCoords(2, 23)
print(pt.getCoords())
print(dir(pt))
# print(pt.x, pt.y)

