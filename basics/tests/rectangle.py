class Rectangle:
    def __init__(self, height=10, width=5):
        self.height = height
        self.width = width

    def calculate_area(self):
        print("Area:", self.height*self.width)

    def draw(self):
        for i in range(self.height):
            print("")
            for ii in range(self.width):
                print("*", end="")


class Square(Rectangle):
    def __init__(self, height=10):
        super(Square, self).__init__(height=height, width=height)


r1 = Rectangle(4, 6)
s1 = Square(2)
r1.draw()