class Robot:
    def __init__(self, name, date, psy, phis):
        self.name = name
        self.date = date
        self.__psy = psy
        self.__phis = phis

    def get_condition(self):
        if self.__psy + self.__phis <= -1:
            print("I feel horrible!")
        elif self.__psy + self.__phis > -1 and self.__psy + self.__phis <= 0:
            print("I feel bad.")
        elif self.__psy + self.__phis > 0 and self.__psy + self.__phis <= 0.5:
            print("Could've been worse.")
        elif self.__psy + self.__phis > 0.5 and self.__psy + self.__phis <= 1:
            print("I think I'm good.")
        else:
            print("I feel amazing!")


unit = Robot("fff", 123, -0.3, -0.8)
unit.get_condition()
