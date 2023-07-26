from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
position = [125,75,25,-25,-75,-125]
all_turtles = []

for index in range(0,6) :
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win, winning color is {winning_color}. ")
            else:
                print(f"You lose, the winning color is {winning_color}.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()