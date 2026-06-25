from turtle import Turtle
import os

SCRIPT_DIR = os.path.dirname(__file__)  # folder where main.py is located
IMAGE_PATH = os.path.join(SCRIPT_DIR, "blank_states_img.gif")
FONT = ("Arial", 10, "bold")

class MapDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(IMAGE_PATH)
        self.penup()

