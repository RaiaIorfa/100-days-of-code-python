from turtle import Screen
from scoreboard import Scoreboard
from map_display import  MapDisplay
from state_pos import StatePos
import os

SCRIPT_DIR = os.path.dirname(__file__)  # folder where main.py is located
IMAGE_PATH = os.path.join(SCRIPT_DIR, "blank_states_img.gif")

screen = Screen()
screen.setup(width=800, height=700)
screen.addshape(IMAGE_PATH)

map_display = MapDisplay()
score = Scoreboard()
state_pos = StatePos()

game_is_on = True
attempts = 0

while game_is_on:
    user_guess = screen.textinput(title="U.S State",prompt="Enter a state:").title()

    if state_pos.check_state(user_guess):
        state_pos.write_state()
        score.increase_count()
        score.update_count()
    elif user_guess == "Exit":
        game_is_on = False
        state_pos.create_csv()
        
    else:
        attempts += 1
        
    if score.count == 50:
        game_is_on = False

screen.mainloop()
