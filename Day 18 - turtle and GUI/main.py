from turtle import Turtle, Screen
import colorgram
from random import randint, choice


timmy = Turtle()
timmy.speed("fastest")
# timmy.hideturtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
colors = colorgram.extract("hirst.jpg", 40)

# test = colors[1].rgb
# timmy.color(test[0], test[1], test[2])
def choose_color():
    global temp
    temp = []
    for each in colors:
        temp.append(each.rgb)

def set_turtle(x, y):
    timmy.penup()
    timmy.setposition(x, y)

def draw_logic():
    timmy.dot(17)
    timmy.forward(45)

def game():
    x = -460.00
    y = -380.00
    set_turtle(x, y)
    choose_color()
    for each in range(0, 18):
        for each in range(0, 21):
            timmy.color(choice(temp))
            draw_logic()
        y += 45
        set_turtle(x, y)
game()
# def randomize_color():
#     timmy.color(choice(colors.rgb))

# def spinograph(amount):
#     angle = 360 / int(amount)
#     for i in range(0, int(amount)):
#         randomize_color()
#         timmy.circle(100)
#         timmy.right(angle)

# user_input = input("how many spins?: ")
# spinograph(user_input)


# # print(colors[2].rgb)




screen.exitonclick()