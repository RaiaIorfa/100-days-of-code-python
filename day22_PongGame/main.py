from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
p1 = Paddle((-350,0))
p2 = Paddle((350,0))

screen.listen()
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()