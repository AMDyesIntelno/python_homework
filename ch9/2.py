import math


class shape:
    def __init__(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetArea(self):
        return 0.0


class Rectangle(shape):
    def __init__(self, x, y, color):
        shape.__init__(self, color)
        self.x = x
        self.y = y

    def GetArea(self):
        return self.x * self.y


class Circle(shape):
    def __init__(self, r, color):
        shape.__init__(self, color)
        self.r = r

    def GetArea(self):
        return math.pi * self.r * self.r


a = Rectangle(1.0, 2.1, "black")
print(a.GetArea())
print(a.GetColor())
b = Circle(3, "green")
print(b.GetArea())
print(b.GetColor())