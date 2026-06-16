from turtle import Turtle

class Paddle(Turtle):
    MOVE_DISTANCE = 20

    def __init__(self, position:tuple):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.MOVE_DISTANCE)
        
