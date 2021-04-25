import time
from random import randint
from turtle import Screen

from map import Map
from tim import Tim
from vehicle import Vehicle


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


s = Screen()
s.colormode(255)
s.setup(600, 600)
s.title("Turtle crossing")
s.tracer(0)

game_is_on = True
tim = Tim()
track = Map()
score = Map()
tipper = Map()
vehicles = []

for vehicle in range(20):
    car = Vehicle(random_color())
    vehicles.append(car)

track.grow_grass()
track.draw_road()

s.listen()
s.onkey(tim.move, "w")


while game_is_on:
    score.update_scoreboard()
    s.update()
    time.sleep(0.1)

    # Show how to play
    if score.level == 1:
        tipper.tip()
    else:
        tipper.clear()

    for vehicle in vehicles:
        vehicle.drive()
        if vehicle.xcor() < -320:
            vehicle.restart_position()

    # Detect if turtle crossed the road
    if tim.ycor() > 250:
        score.update_level()
        tim.come_back()
        for vehicle in vehicles:
            vehicle.speed *= 1.05

    # Detect if turtle hit the car
    for vehicle in vehicles:
        if tim.distance(vehicle) < 15:
            score.game_over()
            game_is_on = False

s.exitonclick()
