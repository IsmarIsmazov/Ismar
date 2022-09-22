class Computer:

    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __mul__(self, make_computations):
        return self.cpu * self.memory

    def __str__(self):
        return f"Cpu: {self.__cpu} memory: {self.__memory}"


class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        return f'Идет звонок на номер {call_to_number} с сим-карты-2: {sim_card_number}'

    def __str__(self):
        return f"sim cards: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return f'на данный момент вы находитесь в {location}'

    def __str__(self):
        return f'Cpu: {self.cpu} Memory: {self.memory} sim cards: {self.sim_cards_list} '


Windows7 = Computer('intel i7', 2000)
Poco_X3 = SmartPhone(2.96, 256, 'MegaCom, Beeline')
iPhone = SmartPhone('Apple A15 Bionic', 512, 'O!, MegaCom')
Nokia3100 = Phone("Beeline")
print(Windows7)
print(Nokia3100.call(1, '099998899'))
print(Poco_X3.use_gps('Цум'))
print(iPhone)
