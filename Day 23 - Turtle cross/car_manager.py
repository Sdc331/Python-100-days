from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(1, 2)
        self.goto(280, random.randrange(-280, 280))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)