# Функторы
"""
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter +=1
        print(self.__counter)
        return self.__counter

c1 = Counter()
c1()
c1()
"""

"""class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0],str):
            raise ValueError("Аргументы должны быть строками")
        return args[0].strip(self.__chars)

s1 = StripChars(" !,.;:")
print(s1(" Hello World! "))

"""

'''
. Создайте функтор для определения порядка сортировки списка p, состоящий из объектов класса Person:
class Person:
    def __init__(self, surname, forename, old):
        self.forename = forename
        self.surname = surname
        self.old = old
 
p = [Person("Иванов", "Иван", 20),
     Person("Петров", "Степан", 21),
     Person("Сидоров", "Альберт", 25)]

То есть, вызывая функтор (пусть он называется SortKey) с названием поля SortKey("surname"), 
сортировка выполнялась бы по этому свойству. 
Если указать сразу два значения: SortKey("surname", "forename"), то сортировка делалась бы по фамилии, 
но при их равенстве – по имени.
(Подсказка: используйте метод sort списка p и его именованный параметр key).

'''

"""
class Person:
    def __init__(self, surname, forename, old):
        self.forename = forename
        self.surname = surname
        self.old = old


p = [Person("Иванов", "Иван", 200),
     Person("Петров", "Степан", 21),
     Person("Сидоров", "Альберт", 25)]


class SortKey:
    def __init__(self, lst):
        self.lst = lst

    def __call__(self, *args):
        self.sortKey = args
        self.lst = sorted(self.lst, key=lambda item: [item.__dict__[key] for key in self.sortKey])
        return print(self.lst[0].forename, self.lst[0].surname, self.lst[0].old, "\n",
                     self.lst[1].forename, self.lst[1].surname, self.lst[1].old, "\n",
                     self.lst[2].forename, self.lst[2].surname, self.lst[2].old, "\n")


c = SortKey(p)

c("forename")
c("surname")
c("old")
"""



"""
v1 = [1, 2, 3]
v2 = [1, 2, 3]


class DefenerVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False




with DefenerVector(v1) as dv:
    for i in range(len(dv)):
        dv[i] += v2[i]

print(v1)
"""





"""
2. Создайте менеджер контекста для безопасной обработки элементов словаря. 
В случае возникновения исключения словарь должен оставаться без изменений. 
Иначе (при успешной работе) он сохранял бы все изменения.
"""
"""
d = {a: a ** 2 for a in range(5)}
print(d)
"""


