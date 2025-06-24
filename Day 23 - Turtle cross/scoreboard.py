from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.level += 1
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, "center", FONT)
