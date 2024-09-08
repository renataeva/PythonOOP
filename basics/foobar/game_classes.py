class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__stamina = stamina
        self.__health = health

    def introduces(self):
        print("================")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.__health}")
        print(f"Stamina: {self.__stamina}")
        print("================")

    def attack(self, target):
        print("================")
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with a sword")
        target.__health -= 3
        print(f"{target.__class__.__name__}'s health is now {target.__health}")
        print("================")

    def herb_heals(self, target=None):
        if not target:
            target = self
        print("================")
        print(f"{self.__class__.__name__} uses healing herbs on {target.__class__.__name__}")
        target.__health += 10
        self.__stamina -= 20
        print(f"{target.__class__.__name__}'s health is now {target.__health}")
        print(f"{self.__class__.__name__} has {self.__stamina} stamina left")
        print("================")

    @property
    def health(self):
        return self.__health

    @property
    def stamina(self):
        return self.__stamina

    @health.setter
    def health(self, new_health):
        self.__health = new_health
        if self.__health > 100:
            self.__health = 100
        if self.__health < 0:
            self.__health = 0

    @stamina.setter
    def stamina(self, new_stamina):
        self.__stamina = new_stamina
        if self.__stamina > 100:
            self.__stamina = 100
        if self.__stamina < 0:
            self.__stamina = 0


class Mage:
    def __init__(self, health=60, mana=100):
        self.__mana = mana
        self.__health = health

    def introduces(self):
        print("================")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.__mana}")
        print("================")

    def attack(self, target):
        print("================")
        print(f"{self.__class__.__name__} harms {target.__class__.__name__} with magic spell")
        target.__health -= 3
        print(f"{target.__class__.__name__}'s health is now {target.__health}")
        print("================")

    def heals(self, target=None):
        if not target:
            target = self
        print("================")
        print(f"{self.__class__.__name__} uses the healing spell on {target.__class__.__name__}")
        target.health += 10
        self.__mana -= 20
        print(f"{target.__class__.__name__}'s health is now {self.health}")
        print(f"{self.__class__.__name__} has {self.mana} mana left")
        print("================")

    @property
    def health(self):
        return self.__health

    @property
    def mana(self):
        return self.__mana

    @health.setter
    def health(self, new_health):
        self.__health = new_health
        if self.__health > 100:
            self.__health = 100
        if self.__health < 0:
            self.__health = 0

    @mana.setter
    def mana(self, new_mana):
        self.__mana = new_mana
        if self.__mana > 100:
            self.__mana = 100
        if self.__mana < 0:
            self.__mana = 0

