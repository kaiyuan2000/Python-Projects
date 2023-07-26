# import colorgram
#
# rgb_list= []
# colors = colorgram.extract("image.jpeg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_list.append(new_color)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(222, 152, 103), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]
turtle.colormode(255)
timmy = Turtle()

def draw_circle():
    timmy.color(random.choice(color_list))
    timmy.begin_fill()
    timmy.circle(10)
    timmy.end_fill()

def draw_10_circle():
    for i in range(0,5):
        draw_circle()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

distance = 50

def draw_all(distance):
    for i in range(0,5):
        timmy.pendown()
        draw_10_circle()
        timmy.penup()
        timmy.home()
        timmy.setheading(90)
        timmy.forward(distance)
        timmy.setheading(0)
        distance = distance + 50

draw_all(distance)

screen = Screen()
screen.exitonclick()