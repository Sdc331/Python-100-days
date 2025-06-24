from turtle import Turtle

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.turtles = []
        self.maxrand = 3
        self.dist = STARTING_MOVE_DISTANCE

    def generate(self):
        car = Turtle(shape="square")
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.shapesize(1,2)
        car.goto(280, random.randrange(-260, 260))
        car.dist = self.dist
        self.turtles.append(car)