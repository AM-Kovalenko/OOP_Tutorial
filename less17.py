# __slots__
import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')  # список (или кортеж) из имен разрешенных свойств

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class PointV(Point2D):
    pass


pt = Point(1, 1)
pt2 = Point2D(2, 2)
pt3 = PointV(3, 3)

