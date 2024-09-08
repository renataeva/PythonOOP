import random

colors = ["red", "blue", "green", "yellow", "magenta", "cyan", "white"]
roles = [0, 1, 2, 3, 4, 5, 6, 7]

class Player:
    def __init__(self, name, colour, role):
        self.name = name
        self.color = colour
        self.role = role

    def set_color(self):
        print("Choose a color:", *colors)
        p_colour = input()
        while p_colour not in colors:
            print("Invalid color. Choose a color:", *colors)
            p_colour = input()
        print(f"You chose {p_colour}")
        colors.pop(colors.index(p_colour))
        self.color = p_colour

    def set_role(self):
        self.role = random.choice(roles)
        if self.role == 0:
            print(f"{self.name} is Imposter")
        else:
            print(f"{self.name} is Crewmate")


player1 = Player("player1", None, None)
player2 = Player("player2", None, None)

player1.set_color()
player1.set_role()
player2.set_color()
player2.set_role()
