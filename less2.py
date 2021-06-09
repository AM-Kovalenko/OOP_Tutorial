class Point3D:
    coords = [0, 0]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def get_coords(self):
        pass

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        Point3D.coords[0] = x
        Point3D.coords[1] = y
        print("координаты изменены")


pt = Point3D(1, 2)

print(pt.coords)
print(pt.x, pt.y)
pt.set_coords(10,10)
print(pt.coords)