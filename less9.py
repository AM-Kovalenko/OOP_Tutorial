class Clock:
    __DAY = 86400  # количество секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("сек должны быть целым числом")

        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # мин
        h = (self.__secs // 3600) % 24  # hour
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0" + str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("правый операнд должен быть Clock")

        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("правый операнд должен быть Clock")

        self.__secs += other.getSeconds()
        return self

    def __eq__(self, other):
        return self.__secs == other.getSeconds()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError(" ключ должен быть строкой")

        if item == "hour":
            return (self.__secs // 3600) % 24
        elif item == "min":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return (self.__secs % 60)


c1 = Clock(6010000)
c2 = Clock(10)

print(c1.getFormatTime())
print(c2.getFormatTime())

c1 += c2
print(c1.getFormatTime())

if c1 != c2:
    print("ok")

print(c1["hour"])