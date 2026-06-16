from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

ball = Ball()
p1 = Paddle((-350,0))
p2 = Paddle((350,0))

screen.listen()
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    ball.move()
    
    # Detect ball wall collision 
    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce_y()
    
    # Detect collision with paddle/pong_stick
    # Detect collision with Right Paddle (p2)
    if ball.distance(p2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with Left Paddle (p1)
    elif ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect ball out of bounds Right Side(p2)
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()

    # Detect ball out of bounds Left Side(p1)
    elif ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()