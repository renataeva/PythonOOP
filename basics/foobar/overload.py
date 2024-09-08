class Warrior():
    def __init__(self, health=100, stamina=100):
        self.__dict__['MAX_HEALTH'] = 100
        self.__dict__['MAX_STAMINA'] = 100
        self.health = health
        self.stamina = stamina
        super(Warrior, self).__init__()

    def __add__(self, target):
        if isinstance(target, int):
            self.heals(self)
        elif isinstance(target, Mage):
            self.heals(target)
        elif isinstance(target, list):
            target.append(self)

    def __sub__(self, target):
        if isinstance(target, Mage):
            self.heals(target)
        elif isinstance(target, list):
            target.remove(self)

    def __setattr__(self, key, value):
        if value > self.MAX_HEALTH:
            self.__dict__[key] = self.MAX_HEALTH
        elif value < 0:
            self.__dict__[key] = 0
        else:
            self.__dict__[key] = value

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} накладывает повязку из',
              f'целебных трав {target.__class__.__name__}')
        self.stamina -= 20
        target.health += 10
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')


class Mage():
    def __init__(self, health=60, mana=120):
        self.__dict__['MAX_HEALTH'] = 60
        self.__dict__['MAX_STAMINA'] = 120
        self.health = health
        self.mana = mana
        super(Mage, self).__init__()

    def __add__(self, target):
        if isinstance(target, int):
            self.heals(self)
        elif isinstance(target, Mage):
            self.heals(target)
        elif isinstance(target, list):
            target.append(self)

    def __sub__(self, target):
        if isinstance(target, Mage):
            self.heals(target)
        elif isinstance(target, list):
            target.remove(self)

    def __setattr__(self, key, value):
        if value > self.MAX_HEALTH:
            self.__dict__[key] = self.MAX_HEALTH
        elif value < 0:
            self.__dict__[key] = 0
        else:
            self.__dict__[key] = value

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
        print('---------------')

    def attacks(self, target):
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')


unit1 = Warrior()
unit2 = Mage()

squad = []
unit1 - unit2
unit1 - 5
unit2 - 10
unit1()
unit2()
