class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        if isinstance(address, Address):
            self.__address = address
        else:
            raise AttributeError("Invalid value for address!\n"
                                 "It must be object of class 'Address'")
        if not isinstance(age, int) or age < 0:
            raise AttributeError("Invalid value for age!")
        else:
            self.__age = age
            self.__was_born()

    def set_age(self, value):
        if not isinstance(value, int) or value < 0:
            raise AttributeError("Invalid value for age!")
        else:
            self.__age = value

    def get_age(self):
        return self.__age

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def __was_born(self):
        print(f"Родился {self.__name}")

    def info(self):
        return f"Name: {self.__name} Age: {self.__age}\n" \
               f"City: {self.__address.city} Street: {self.__address.street}" \
               f"Number: {self.__address.number}\n"

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, address, command):
        super().__init__(name, age, address)
        self.__command = command

    @property
    def command(self):
        # print("Работает геттер property")
        return self.__command

    @command.setter
    def command(self, value):
        # print("Работает setter property")
        self.__command = value

    def speak(self):
        print(f"Dog {self.get_name()} says - Gav Gav")

    def info(self):
        return super().info() + f"Command: {self.__command}"


class Cat(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)

    def speak(self):
        print(f"Cat {self.get_name()} says - Meow Meow")


class Fish(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)


class Cow:
    def speak(self):
        pass


cow1 = Cow()

# animal = Animal("Animal", 1)
# print(animal.info())
#
# # animal.age = "Пять"
# animal.set_age(8)
#
# print(animal.get_age())
# print(animal.info())

address1 = Address("Bishkek", "Ibraimova", 103)


def create_animals():
    ak_tosh = Dog("Ak-Tosh", 3, address1, 'sit')
    barbados = Dog("Barbados", 2, address1, 'aport')
    muhtar = Dog("muhtar", 5, address1, 'sit')

    barsik = Cat("Baaarsik", 1, address1)
    murka = Cat("murka", 1, address1)
    snezhok = Cat("snezhok", 1, address1)

    dorri = Fish("Dorri", 1, address1)

    animals = [ak_tosh, barsik, barbados, murka, muhtar, snezhok, dorri]
    return animals


for animal in create_animals():
    animal.speak()
    print(animal.info())
