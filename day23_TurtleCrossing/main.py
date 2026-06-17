import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkey(player.move, "Up")
screen_edge = (0,300)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Detect collison with wall
    if player.distance(screen_edge) < 20:
        player.reset_turtle()
        
    # Detect collision with car
    screen.update() 
