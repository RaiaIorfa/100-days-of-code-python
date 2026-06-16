from turtle import Turtle, Screen
import random

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)

def dashed_line():
    # Draw a line of 10 paces and a gap of 10 paces 15 times
    for _ in range(15):
        timmy.color(random_color())
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_multi_polygon(num_shapes):
    # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon.
    count = 3
    timmy.teleport(x=-50, y=100)
    timmy.pensize(2)
    while count <= num_shapes:
        timmy.color(random_color())
        for _ in range(count):
            timmy.forward(100)
            timmy.right(360 / count)
        count += 1

# def random_walk(steps):
#     timmy.hideturtle()
#     timmy.pensize(10)
#     timmy.speed(10)

#     direction = ["up", "down", "forward", "right"]
#     for _ in range(steps):
#         timmy.setheading(0)
#         move = random.choice(direction)
#         timmy.pencolor(random_color())
#         if move == "up":
#             timmy.left(90)
#             timmy.forward(25)
#         elif move == "down":
#             timmy.right(90)
#             timmy.forward(25)
#         elif move == "forward":
#             timmy.forward(25)
#         else:
#             timmy.backward(25) 
def random_walk(steps):
    timmy.speed("fastest")
    timmy.width(15)
    direction = [0, 90, 180, 270]
    for _ in range(steps):
        timmy.pencolor(random_color())
        timmy.setheading(random.choice(direction))
        timmy.forward(25)

def spirograph():
    direction = 0
    step = 90
    timmy.speed("fastest")
    for _ in range(step):
        timmy.color(random_color())
        timmy.circle(100)
        direction += 4
        timmy.setheading(direction)

screen = Screen()
timmy = Turtle()
screen.colormode(255)
screen.setup(1.0, 1.0)

timmy.shape("turtle")
timmy.shape("arrow")
timmy.width(1.3)
timmy.hideturtle()
timmy.shapesize(0.6, 0.6, 1)

dashed_line()
# draw_multi_polygon(12)
# random_walk(200)
# spirograph()

# timmy.forward(40)
# timmy.circle(100)




screen.exitonclick()