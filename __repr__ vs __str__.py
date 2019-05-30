import datetime


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'A {self.color} {self.__class__.__name__}(class), {self.mileage} mileage. / __repr__'

    # if no __str__ it prints __repr__
    # def __str__(self):
    #     return f'A {self.color} car. / __str__'


my_car = Car('red', 32765)
print(my_car)
print(repr(my_car))


# today = datetime.date.today()

# print(str(today))  # __str__ -> easy to read for humans
# print(repr(today))  # __repr__ -> unambiguous
