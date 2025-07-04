import pandas
from turtle import Turtle, Screen
### ------- Initial turtle / screen setup -------
my_screen = Screen()
my_screen.setup(700, 500)
my_screen.title("U.S. States Game")
my_screen.bgpic("blank_states_img.gif")
my_turtle = Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
### ------- Hold state information to check against user input later ------

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

score = 0
user_guesses = []
to_learn = []
game_is_on = True
while game_is_on:
    ans = my_screen.textinput(f"{score}/50 States Guessed", "Name a state:").title()

### ------------- Check whether answer is valid and not yet guessed --------
    if ans == "Exit":
         to_learn = [state for state in states if state not in user_guesses]
         pandas.DataFrame(to_learn).to_csv("Homework states.csv")
         break
    if ans in states and ans not in user_guesses:
            state_data = data[data.state == ans]
            my_turtle.goto(state_data.x.item(), state_data.y.item())
            my_turtle.write(ans)
            score += 1

    user_guesses.append(ans)
    if score >= 50:
        my_turtle.goto(0, 0)
        my_turtle.write("You won!")
        game_is_on = False


my_screen.exitonclick()