class Square:
    def __init__(self, a):
        self.a = a

    def getArea(self):
        return self.a*self.a

class Circle:
    def __init__(self, r):
        self.r = r

    def getArea(self):
        return 3.14*self.r*self.r

s = Square(2)
c = Circle(1)

print(s.getArea())
print(c.getArea())
