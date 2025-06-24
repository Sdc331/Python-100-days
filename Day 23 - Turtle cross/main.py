import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
my_score = Scoreboard()
my_player = Player()
cars = CarManager()

pace = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkey(my_player.move, "Up")
    if pace == 0 or pace % 8 == 0:
        for each in range(random.randrange(0, cars.maxrand)):
            cars.generate()
    pace += 1
    for each in cars.turtles:
        each.forward(each.dist)
## ------------- Advance to the next round. Reset game's state, increase cars speed --------------
    if my_player.ycor() >= 280:
        my_player.reset()
        for each in cars.turtles:
            each.hideturtle()
            each.goto(500, 500)
        cars.dist += 5
        cars.maxrand += 1
        pace = 0
        my_score.level_up()
    for each in cars.turtles:
        if each.distance(my_player) < 30:
            game_is_on = False
            my_score.game_over()
    screen.update()
    


screen.exitonclick()