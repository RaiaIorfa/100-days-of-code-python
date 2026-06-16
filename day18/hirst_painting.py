# import colorgram
import random
from turtle import Turtle, Screen 

rgb_colors = [(242, 241, 238), (240, 242, 245), (244, 238, 241), (235, 243, 239), (119, 167, 203), (28, 99, 158), (219, 211, 101), (179, 83, 45), (213, 166, 85), (53, 31, 51), (153, 174, 27), (170, 23, 19), (215, 138, 154), (225, 87, 47), (168, 27, 35)]

# Commented Code to extract color palete as object instances from image using colorgram.py
# extracted_colors = colorgram.extract("image.png", 15)
# for obj in extracted_colors:
#     rgb_colors.append((obj.rgb.r, obj.rgb.g, obj.rgb.b))

def hirst_painting(colors):
    screen.colormode(255)
    t.speed("fastest")
    t.hideturtle()
    count = 0
    x_position = t.xcor() - 250
    y_postion = t.ycor() - 250
    t.teleport(x_position, y_postion)
    while count < 10:
        for _ in range(10):
            t.color(random.choice(colors))
            t.begin_fill()
            t.pendown()
            t.circle(10)
            t.end_fill()
            t.penup()
            t.forward(50)
        count += 1
        y_postion += 50

        t.teleport(x_position, y_postion)

t=Turtle()
screen = Screen()
screen.setup(1.0,1.0)
hirst_painting(rgb_colors)

screen.exitonclick()
