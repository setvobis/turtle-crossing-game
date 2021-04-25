from random import randrange
from turtle import Turtle


class Vehicle(Turtle):

    def __init__(self, color):
        super(Vehicle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.pu()
        self.setpos(randrange(-300, 300, 45), randrange(-220, 220, 25))
        self.fillcolor(color)
        self.speed = 10

    def drive(self):
        new_x = self.xcor() - self.speed
        self.setx(new_x)

    def restart_position(self):
        self.setpos(randrange(320, 340, 45), randrange(-220, 220, 25))
