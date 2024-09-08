from basics.inheritance.encapsulation import Warrior, Mage
import random


class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        self.__armor = armor
        print(self.__armor)
        self.__health = health
        self.__stamina = stamina
        super().__init__(health, stamina)


    def attack(self, target):
        if random.randint(1, 10) <= 4:
            self.print_line()
            print(f"{self.__class__.__name__} makes a critical hit on {target.__class__.__name__}")
            self.__critical_hit(target)
            print(f"{target.__class__.__name__}'s health is now {target._get_health()}")
            self.print_line()
        else:
            super().attack(target)

    def _set_health(self, points):
        if points > 0:
            self.__health += points
        elif points < 0:
            if self.__armor <= 0:
                self.__health -= points
            self.__armor -= points


    def __critical_hit(self, target):
        target._set_health(-10)


class Wizard(Mage):
    def __init__(self, health=100, shield=100, stamina=100):
        self.__shield = shield
        print(self.__armor)
        self.__health = health
        self.__stamina = stamina
        super().__init__(health, stamina)


    def attack(self, target):
        if random.randint(1, 10) <= 4:
            self.print_line()
            print(f"{self.__class__.__name__} sends a fireball {target.__class__.__name__}")
            self.__critical_hit(target)
            print(f"{target.__class__.__name__}'s health is now {target._get_health()}")
            self.print_line()
        else:
            super().attack(target)

    def _set_health(self, points):
        if points > 0:
            self.__health += points
        elif points < 0:
            if self.__shield <= 0:
                self.__health -= points
            self.__shield -= points


    def __critical_hit(self, target):
        target._set_health(-15)


unit1 = Knight(50, 0, 50)
unit2 = Knight(50, 50, 50)
unit2.attack(unit1)
