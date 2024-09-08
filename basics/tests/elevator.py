class Elevator():
    def __init__(self, levels=5, level_current=3):
        self.levels = levels
        self.level_current = level_current

    def up(self):
        if self.level_current == self.levels:
            print("You can't go higher")
        else:
            self.level_current+=1
            print(f"You are now on the floor No{self.level_current}")

    def down(self):
        if self.level_current == 1:
            print("You can't go lower")
        else:
            self.level_current-=1
            print(f"You are now on the floor No{self.level_current}")

    def move(self, request):
        if request < 1 or request > self.levels:
            print("You cannot go there, floor not found")
        else:
            self.level_current = request
            print(f"You are now on the floor No{self.level_current}")

e1 = Elevator()
e2 = Elevator(7, 5)

e1.move(5)
e2.move(10)
