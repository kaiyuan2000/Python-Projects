from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(x= -270, y=260)
        self.write(f"Level : {self.level}",align= "left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=-0, y=0)
        self.write("Game Over", align="center", font=FONT)

