from turtle import Turtle
FONT1 = ("Arial", 14, "bold")
FONT2 = ("Arial", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.count = 0
        self.update_count()
    
    def update_count(self):
        self.clear()
        self.goto(x=-350, y=320)
        self.write(arg="SCORE:", align="center", font=FONT1)
        self.goto(x=-355, y=300)
        self.write(arg=f"{self.count} / 50", align="center", font=FONT2)

    def increase_count(self):
        self.count += 1