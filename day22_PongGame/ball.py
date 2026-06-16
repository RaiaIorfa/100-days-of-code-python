from turtle import Turtle
import random

class Ball(Turtle):
    MOVE_DISTANCE = 10
    def __init__(self):
        super().__init__(shape ="square")
        self.color("white")
        self.penup()
        # self.direction = self.heading()
        
    def move(self, direction = ""):
        if direction == "top_left":
            new_x = self.xcor() + self.MOVE_DISTANCE
            new_y = self.ycor() - self.MOVE_DISTANCE
        elif direction == "top_right":
            new_x = self.xcor() - self.MOVE_DISTANCE
            new_y = self.ycor() - self.MOVE_DISTANCE
        elif direction == "bottom_right":
            new_x = self.xcor() + self.MOVE_DISTANCE
            new_y = self.ycor() + self.MOVE_DISTANCE
        elif direction == "bottom_left":
            new_x = self.xcor() - self.MOVE_DISTANCE
            new_y = self.ycor() + self.MOVE_DISTANCE
        else:
            new_x = self.xcor() + self.MOVE_DISTANCE
            new_y = self.ycor() + self.MOVE_DISTANCE

        self.goto(new_x, new_y)

        # if self.direction >= 0 and self.direction < 90:
        #     self.goto(self.xcor() + self.MOVE_DISTANCE, self.ycor() + self.MOVE_DISTANCE)
        # elif self.direction >= 90 and self.direction < 180:
        #     self.goto(self.xcor() - self.MOVE_DISTANCE, self.ycor() + self.MOVE_DISTANCE)
        # elif self.direction >= 180 and self.direction < 270:
        #     self.goto(self.xcor() - self.MOVE_DISTANCE, self.ycor() - self.MOVE_DISTANCE)
        # elif self.direction >= 270:
        #     self.goto(self.xcor() + self.MOVE_DISTANCE, self.ycor() - self.MOVE_DISTANCE)

    def bounce(self, boundary):
        if boundary == "top":
            if self.xcor() > 300 - self.xcor():
                return "top_left"
            else:
                return "top_right"
        elif boundary == "bottom":
            if self.xcor() > 300 - self.xcor():
                return "bottom_left"
            else:
                return "bottom_right"


    