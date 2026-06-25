from turtle import Turtle
import pandas as pd
import csv
import os

SCRIPT_DIR = os.path.dirname(__file__)  # folder where main.py is located
IMAGE_PATH = os.path.join(SCRIPT_DIR, "blank_states_img.gif")
FONT = ("Arial", 10, "bold")

class StatePos(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.x_pos = 0 
        self.y_pos = 0
        self.state = ""
        self.checked_states = []
        self.unchecked_states = []
        self.us_state_df = pd.read_csv("50_states.csv")

    def check_state(self, state_input):
        for row in self.us_state_df.itertuples(index=False):
            if state_input.title() in self.checked_states:
                return False
            if state_input.title() == row.state:
                self.x_pos = row.x
                self.y_pos = row.y 
                self.state = row.state
                self.checked_states.append(row.state)
                return True
        return False
    
    def create_csv(self):
        state_lists = self.us_state_df["state"].tolist()
        for item in state_lists:
            if item not in self.checked_states:
                self.unchecked_states.append(item)
        
        with open("states_to_learn.csv", mode="w", newline='') as file:
            writer = csv.writer(file)
            # create the first row as column label
            writer.writerow(["States_Missed"])
            # go through the unchecked_states lists and write each item in its own row
            for state in self.unchecked_states:
                writer.writerow([state])
                
    def write_state(self):
        self.goto(x=self.x_pos, y=self.y_pos)
        self.write(arg=f"{self.state}", align="center", font=FONT)

