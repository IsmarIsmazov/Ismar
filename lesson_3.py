



class MusicPlayable:
    @staticmethod
    def play_music(song):
        print(f"играет музыка {song}...")


class Car(MusicPlayable):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print("Машина едет... ")

    def __str__(self):
        return f"MOdel: {self.model} Year: {self.year}"


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f"Машина {self.model} едет на электричестве... ")

    def __str__(self):
        return super(ElectricCar, self).__str__() + f" battery: {self.battery}"


class FuelCar(Car):
    __total_fuel = 5000

    @staticmethod
    def fuel_type():
        print("AI - 95")

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f"Машина {self.model} едет на топливе... ")

    def __str__(self):
        return super(FuelCar, self).__str__() + f" fuel_bank: {self.fuel_bank}"

    def __gt__(self, other):
        return self.fuel_bank > other.fuel_bank and self.year > other.year

    def __ge__(self, other):
        return self.fuel_bank >= other.fuel_bank

    def __eq__(self, other):
        return self.year == other.year

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank

    def __sub__(self, other):
        return self.fuel_bank - other.fuel_bank

    def __mul__(self, other):
        return self.fuel_bank * other.fuel_bank


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, fuel_bank, battery):
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_bank)


class Laptop(MusicPlayable):
    pass


print(FuelCar.get_total_fuel())

tesla = ElectricCar("Tesla model X", 2022, 80000)
mersedes = FuelCar("Mersedes-Benz s500", 2020, 40)

toyota = HybridCar("Toyota Camry", 2020, 90, 50000)
print(FuelCar.get_total_fuel())

laptom = Laptop()

print(tesla)
print(mersedes)

print(toyota)

toyota.drive()
toyota.play_music("Morgenshtern - IcE")
laptom.play_music("Руки вверх - 18")

toyota.fuel_type()
FuelCar.fuel_type()
# print(HybridCar.__mro__)
# print(HybridCar.mro())

# num1 = 84
# num2 = 98
# print(num2 > num1)

print(toyota * mersedes)
