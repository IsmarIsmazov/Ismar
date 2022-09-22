# OOP - Object oriented programming
class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color


class Plane(Transport):  # DRY - Don't Repeat Yourself
    def __init__(self, model, year, color):
        Transport.__init__(self, model, year, color)
        # super().__init__(model, year, color)


class Car(Transport):
    wheels = 4  # Аттрибуты класса

    def __init__(self, model, year, color, penalties=0.0):  # Конструктор
        Transport.__init__(self, model, year, color)
        self.penalties = penalties

    def drive(self, city):  # Метод
        print(f"Машина {self.model} едет в {city}")

    def change_color(self, new_color):
        self.color = new_color

    def show_car(self):
        print(f"Model: {self.model} Year: {self.year} "
              f"Color: {self.color} Penalties: {self.penalties}")


class Track(Car):
    """Это класс для грузовика"""
    wheels = 6  # Классовый аттрибут

    def __init__(self, model, year, color, load_capacity, penalties=0.0):
        Car.__init__(self, model, year, color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, product, weight):
        if weight > self.load_capacity:
            print(f"Вы не можете загрузить этот груз "
                  f"Максимальная грузоподьемность {self.load_capacity}!")
        else:
            print(f"{product} ({weight} кг) загружен в грузовик {self.model}")

    def show_car(self):
        print(
            f"Model: {self.model} Year: {self.year} Color: {self.color} "
            f"Penalties: {self.penalties} Load capacity: {self.load_capacity}")


audi_car = Car("Audi A6", 2020, "White", 300.5)
lada_car = Car(color="Blue", model="Lada 2106", year=1999)

print(audi_car)
# print(f"Model: {audi_car.model} Year: {audi_car.year} Color: {audi_car.color} P: {audi_car.penalties}")

audi_car.color = "Yellow"
audi_car.change_color("Black")

# print(f"Model: {audi_car.model} Year: {audi_car.year} Color: {audi_car.color}")

audi_car.drive("Бишкек")
lada_car.drive("Алмата")

print(Car.wheels)

man_track = Track(model="Man 3", year=2014, color="Red", penalties=200, load_capacity=2000)

man_track.load_cargo("Алма", 9990)
man_track.show_car()
audi_car.show_car()
lada_car.show_car()
print(man_track.wheels)
print(Track.__doc__)
