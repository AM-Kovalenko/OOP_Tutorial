# 6 Простое наследование классов

"""
1. Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки». В базовом
классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные свойства:

для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль.

"""

"""
class PersonalComputer:
    def __init__(self, model='a', memory_size=0, hdd_size=0, cpu='c'):
        self._model = model
        self._memory_size = memory_size
        self._hdd_size = hdd_size
        self.__cpu = cpu

    def getCPU(self):
        return self.__cpu

class Notebook(PersonalComputer):
    def __init__(self, dimensions=0, diag=0, *args):
        self.dimensions = dimensions
        self.diag = diag
        super().__init__(*args)

    def printInfo(self):
        print(f"dimensions:{self.dimensions}, diag:{self.diag}")


class TablePC(PersonalComputer):
    def __init__(self,*args, display=0, keyboard='k', mouse='m'):               #переопределение констркутра
        self.display = display
        self.keyboard = keyboard
        self.mouse = mouse
        PersonalComputer.__init__(self, *args)

    def printInfo(self):
        print(f"dimensions:{self.display}, diag:{self.keyboard}, mouse:{self.mouse}, CPU:{super().getCPU()}")

"""


"""
2. Повторите это задания для суперкласса «Человек» и подклассов «Мужчина» и «Женщина». 
Подумайте, какие общие характеристики можно выделить в суперкласс и какие частные свойства указать в подклассах.
"""
