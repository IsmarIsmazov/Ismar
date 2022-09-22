import random


class SuperAbiliti:
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_NEVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
             self.__health = 0

        else:
            pass

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_abiliti):
        super(Hero, self).__init__(name, health, damage)
        self.super_abiliti = super_abiliti

    def hit(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbiliti.CRITICAL_DAMAGE)


class Mag(Hero):
    def __init__(self, name, health, damage):
        super(Mag, self).__init__(name, health, damage, SuperAbiliti.BOOST)


class Medic(Hero):
    def __init__(self, name, health, damage):
        super(Medic, self).__init__(name, health, damage, SuperAbiliti.HEAL)


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbiliti.SAVE_DAMAGE_AND_NEVERT)


def print_statistics(boss, heroes):
    print()
