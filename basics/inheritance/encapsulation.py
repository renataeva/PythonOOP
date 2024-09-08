class Logger:
    PL = "================"

    def print_line(self):
        print(self.PL)


class Warrior(Logger):
    def __init__(self, health=100, stamina=100):
        self.__stamina = stamina
        self.__health = health

    def introduces(self):
        self.print_line()
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.__health}")
        print(f"Stamina: {self.__stamina}")
        self.print_line()

    def attack(self, target):
        if target._get_health() <= 3:
            target._set_health(-3)
            self.print_line()
            print(f"{self.__class__.__name__} fatally harms {target.__class__.__name__} with a sword")
            print(f"{target.__class__.__name__} is now out of the game")
            self.print_line()
        self.print_line()
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with a sword")
        target._set_health(-3)
        print(f"{target.__class__.__name__}'s health is now {target._get_health()}")
        self.print_line()

    def herb_heals(self, target=None):
        if not target:
            target = self
        if self.__stamina - 20 < 0:
            self.print_line()
            print("You don't have enough energy to heal.")
            return
        self.print_line()
        print(f"{self.__class__.__name__} uses healing herbs on {target.__class__.__name__}")
        target._set_health(10)
        self.__stamina -= 20
        print(f"{target.__class__.__name__}'s health is now {target._get_health()}")
        print(f"{self.__class__.__name__} has {self.__stamina} stamina left")
        self.print_line()

    def _get_health(self):
        return self.__health

    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        if self.__health < 0:
            self.__health = 0


class Mage(Logger):

    def __init__(self, health=60, mana=100):
        self.__mana = mana
        self.__health = health

    def introduces(self):
        self.print_line()
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.__health}")
        print(f"Mana: {self.__mana}")
        self.print_line()

    def attack(self, target):
        if target._get_health() <= 3:
            target._set_health(-3)
            self.print_line()
            print(f"{self.__class__.__name__} fatally harms {target.__class__.__name__} with magic")
            print(f"{target.__class__.__name__} is now out of the game")
            self.print_line()
        self.print_line()
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with magic spell")
        target._set_health(-3)
        print(f"{target.__class__.__name__}'s health is now {target._get_health()}")
        self.print_line()

    def heals(self, target=None):
        if not target:
            target = self
        if self.__mana - 20 < 0:
            print("You don't have enough energy to heal.")
            return
        self.print_line()
        print(f"{self.__class__.__name__} uses the healing spell on {target.__class__.__name__}")
        target._set_health(-10)
        self.__mana -= 20
        print(f"{target.__class__.__name__}'s health is now {self.__health}")
        print(f"{self.__class__.__name__} has {self.__mana} mana left")
        self.print_line()

    def _get_health(self):
        return self.__health

    def _set_health(self, points):
        self.__health += points
        if self.__health > 60:
            self.__health = 60
        if self.__health < 0:
            self.__health = 0
