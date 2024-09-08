from basics.foobar.game_classes import Warrior, Mage
import random


class Archer(Warrior):

    DAM_SIM = 3

    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows

    def introduces(self):
        super().introduces()
        print(f"Arrows: {self.arrows}")
        print("================")

    def _normal_attack(self, target):
        print("================")
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with a bow")
        target.health -= self.DAM_SIM
        self.arrows -= 1
        print(f"{target.__class__.__name__}'s health is now {target.health}")
        print(f"{self.__class__.__name__} has {self.arrows} arrows left")
        print("================")

    @staticmethod
    def _is_critical_attack():
        return random.randint(1, 10) <= 3

    def attack(self, target):
        if self._is_critical_attack():
            self._critical_attack(target)
        else:
            self._normal_attack(target)

    def _critical_attack(self, target):
        print("================")
        print(f"{self.__class__.__name__} makes a critical hit on {target.__class__.__name__}")
        self.__critical_hit(target)
        print(f"{target.__class__.__name__}'s health is now {target.health}")
        print("================")

    def __critical_hit(self, target):
        target.health -= 15
        self.stamina -= 30


class Alchemist(Mage):
    def __init__(self, health=100, stamina=100, flasks=10):
        super().__init__(health, stamina)
        self.flasks = flasks

    def introduces(self):
        super().introduces()
        print(f"Fire flasks: {self.flasks}")
        print("================")

    def attacks(self, target):
        print("================")
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with a fire flask, but hits themself too.")
        target.health -= 10
        self.health -= 3
        self.flasks -= 1
        print(f"{target.__class__.__name__}'s health is now {target.health}")
        print(f"{self.__class__.__name__}'s health is now {self.health}")
        print(f"{self.__class__.__name__} has {self.flasks} fire flasks left")
        print("================")


alchemist = Alchemist()
archer = Archer()
archer.introduces()

archer.attack(alchemist)
archer.introduces()

archer.attack(alchemist)
