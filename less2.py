"""
1. Создайте класс Point3D, который хранит координаты в виде списка.
Пропишите у него конструктор для создания экземпляров с локальными координатами.
Также добавьте методы, позволяющие изменять координаты и получать их (в виде кортежа).
"""


class Point3D:
    coords = [0, 0]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coords(self):
        print(tuple(Point3D.coords))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        Point3D.coords[0] = x
        Point3D.coords[1] = y
        print("координаты изменены")


'''
pt = Point3D(1, 2)
print(pt.coords)
print(pt.x, pt.y)
pt.set_coords(10, 10)
print(pt.coords)
pt.get_coords()

'''

"""
2. Объявите класс Point с конструктором, который бы позволял создавать экземпляр на основе другого, уже существующего. 
Если аргументы в конструктор не передаются, то создается объект с локальными атрибутами по умолчанию.
"""
'''
class Point:

    def __init__(self, name=''):
        name = Point3D()

        print(name.coords)
        #ex = self.name2
        #ex= Point()
        #print(ex)

p = Point()

'''

"""
3. Напишите программу, в которой пользователь вводит координаты x, y с клавиатуры, 
создается соответствующий экземпляр и он сохраняется в списке. 
Количество вводимых объектов N=5. Затем, вывести их атрибуты в консоль.

"""
lst = []
for n in range(5):
    x, y = map(int, input("Введите x y: ").split())
    print(x, y)
    pt = Point3D(x, y)
    lst.append(pt)

for i in range(len(lst)):
    print(lst[i].x, lst[i].y)
