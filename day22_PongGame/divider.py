from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -400)
        self.pendown()
        self.setheading(90)
        self.draw_dash()


    
    def draw_dash(self):
        self.width(3)
        for _ in range(100):
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()
    