from turtle import Turtle

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor()+ self.xmove
        new_y = self.ycor()+ self.ymove
        self.goto(new_x,new_y)
        #self.setheading(45)
        #self.forward(20)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.xmove *= -1
        self.speed = 0.1


