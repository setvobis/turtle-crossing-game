from turtle import Turtle


class Map(Turtle):

    def __init__(self):
        super(Map, self).__init__()
        self.ht()
        self.color("black")
        self.pu()
        self.level = 1
        self.setpos(-240, 260)

    def grow_grass(self):
        self.color((51, 204, 51))
        self.goto(-310, -310)
        self.begin_fill()
        for i in range(3):
            self.fd(620)
            self.lt(90)
        self.end_fill()

    def draw_road(self):
        self.color("grey")
        self.goto(-300, -230)
        self.begin_fill()
        self.goto(310, -230)
        self.goto(310, 230)
        self.goto(-300, 230)
        self.goto(-300, -230)
        self.end_fill()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 18, "normal"))

    def update_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def tip(self):
        self.goto(-280, -270)
        self.write("Cross the road and dont get hit by a car     "
                   "Press 'W' to move", align="left", font=("Arial", 12, "normal"))