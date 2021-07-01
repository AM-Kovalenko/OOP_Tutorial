# Моно состояние

class CarA6C5:
    __characteristics = {
        'veight': 1500,
        'company' : 'VAG',
        'owner' : 'KA',
    }

    def __init__(self):
        self.__dict__ = CarA6C5.__characteristics

a1 = CarA6C5()
a2 = CarA6C5()
a3 = CarA6C5()

print(a1.veight)
a2.veight = '1000'
print(a3.veight)