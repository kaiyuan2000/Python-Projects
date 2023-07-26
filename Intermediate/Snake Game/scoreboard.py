from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as f:
            self.highscore = int(f.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
