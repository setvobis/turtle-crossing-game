from turtle import Turtle


class Tim(Turtle):

    def __init__(self):
        super(Tim, self).__init__()
        self.shape("turtle")
        self.pencolor("yellow")
        self.fillcolor((51, 153, 51))
        self.pu()
        self.seth(90)
        self.come_back()

    def move(self):
        self.forward(25)

    def come_back(self):
        self.setpos(0, -275)
