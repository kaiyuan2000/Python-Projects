import time
import turtle
import pandas

STATE = 50

#setup of the game
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#setup pen to write on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

#variable
score = 0

#read data
data = pandas.read_csv("50_states.csv")
data_state = data["state"]
states  = []

game_is_on = True
while game_is_on:
    #prompt for input
    answer_state = screen.textinput(title=f"{score}/{STATE} Guess the State", prompt="What's another state's name?").title()
    #loop over all the states to find whether match
    for correct_state in data_state:
        if answer_state.lower() == correct_state.lower() and (answer_state not in states):
            states.append(answer_state)
            score += 1
            #the row of correct state
            corrected_state = data[data["state"] == correct_state]
            pen.goto(x=int(corrected_state["x"]), y=int(corrected_state["y"]))
            pen.write(correct_state, align="center", font=("Courier", 10, "normal"))
        else :
            pass
    #winning condition
    if score == 50:
        pen.goto(0,0)
        pen.write("Congratz, you have won the game",align="center", font=("Courier", 30, "normal"))
        time.sleep(5)
        game_is_on = False

    if answer_state == "Exit":
        break

missing_states = []
for state in data_state:
    if state not in states:
        missing_states.append(state)

df = pandas.DataFrame(missing_states)
df.to_csv("missing states.csv")


