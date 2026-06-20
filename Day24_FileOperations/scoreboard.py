from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.read_file()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def read_file(self):
        with open("data.txt") as open_data:
            self.high_score = int(open_data.read())
    
    def update_score(self):
        self.score += 1
        self.display_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as open_data:
                open_data.write(str(self.high_score))
        self.score = 0
        self.display_score()