from turtle import  Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game program")
screen.tracer(0)


paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle_r.go_up, key= "Up")
screen.onkey(fun=paddle_r.go_down, key="Down")
screen.onkey(fun=paddle_l.go_up, key= "w")
screen.onkey(fun=paddle_l.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    #detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        #bounce the ball
        ball.bounce_y()

    #detect collision with_paddle
    if ball.distance(paddle_r)  < 50 and ball.xcor() > 330 or ball.distance(paddle_l)  < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #detect out of bounds
    if ball.xcor()> 380:
        ball.reset()
        scoreboard.l_point()

    elif ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()