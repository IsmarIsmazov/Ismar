import random


class SuperAbility:
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_NEVERT = 4
    STUN_ATTACK = 5
    TAKE_DAMAGE = 6
    SACRIFISE = 7
    INVIS_AND_RETURN_DAMAGE = 8
    growth_change = 9
    BAFF_DEBAFF = 10


class GameEntity:
    def __init__(self, name, hp, damage):
        self.__name = name
        self.__hp = hp
        self.damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        pass

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value


class Boss(GameEntity):
    def __init__(self, name, hp, damage):
        super(Boss, self).__init__(name, hp, damage)
        self.__defense = None

    @property
    def defense(self):
        return self.__defense

    def choose_defense(self, heroes):
        selected_hero = random.choice(heroes)
        self.__defense = selected_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            hero -= self.damage


class Hero(GameEntity):
    def __init__(self, name, hp, damage, super_ability):
        super(Hero, self).__init__(name, hp, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        boss.hp -= self.damage


class Warrion(Hero):
    def __init__(self, name, hp, damage):
        super(Warrion, self).__init__(name, hp, damage, SuperAbility.CRITICAL_DAMAGE)


class Mag(Hero):

    def __init__(self, name, hp, damage):
        super(Mag, self).__init__(name, hp, damage, SuperAbility.BOOST)


class Medic(Hero):

    def __init__(self, name, hp, damage):
        super(Medic, self).__init__(name, hp, damage, SuperAbility.HEAL)


class Berserk(Hero):

    def __init__(self, name, hp, damage):
        super(Berserk, self).__init__(name, hp, damage, SuperAbility.SAVE_DAMAGE_AND_NEVERT)


class Thor(Hero):

    def __init__(self, name, hp, damage):
        super(Thor, self).__init__(name, hp, damage, SuperAbility.STUN_ATTACK)


class Golem(Hero):

    def __init__(self, name, hp, damage):
        super(Golem, self).__init__(name, hp, damage, SuperAbility.TAKE_DAMAGE)


class Avrora(Hero):

    def __init__(self, name, hp, damage):
        super(Avrora, self).__init__(name, hp, damage, SuperAbility.INVIS_AND_RETURN_DAMAGE)


class Witcher(Hero):

    def __init__(self, name, hp, damage):
        super(Witcher, self).__init__(name, hp, damage, SuperAbility.SACRIFISE)


class Druid(Hero):

    def __init__(self, name, hp, damage):
        super(Druid, self).__init__(name, hp, damage, SuperAbility.BAFF_DEBAFF)


class AntMen(Hero):

    def __init__(self, name, hp, damage):
        super(AntMen, self).__init__(name, hp, damage, SuperAbility.SAVE_DAMAGE_AND_NEVERT)


def print_statistics(boss, heroes):
    print()
