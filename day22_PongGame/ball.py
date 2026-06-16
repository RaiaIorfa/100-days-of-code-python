from turtle import Turtle
import random

class Ball(Turtle):
    # MOVE_DISTANCE = 10
    def __init__(self):
        super().__init__(shape ="square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(f"Moving To: \n new Y-cooridinate: {new_y} | new X-coordinate: {new_x}")
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        # print(f"Y-cooridinate: {self.ycor()} | X-coordinate: {self.xcor()}")
        # print("_" * 100)


    # def move(self, direction = ""):
    #     if direction == "top_left":
    #         new_x = self.xcor() + self.MOVE_DISTANCE
    #         new_y = self.ycor() - self.MOVE_DISTANCE
    #     elif direction == "top_right":
    #         new_x = self.xcor() - self.MOVE_DISTANCE
    #         new_y = self.ycor() - self.MOVE_DISTANCE
    #     elif direction == "bottom_right":
    #         new_x = self.xcor() + self.MOVE_DISTANCE
    #         new_y = self.ycor() + self.MOVE_DISTANCE
    #     elif direction == "bottom_left":
    #         new_x = self.xcor() - self.MOVE_DISTANCE
    #         new_y = self.ycor() + self.MOVE_DISTANCE
    #     else:
    #         new_x = self.xcor() + self.MOVE_DISTANCE
    #         new_y = self.ycor() + self.MOVE_DISTANCE

    #     self.goto(new_x, new_y)

    # def bounce(self, boundary):
    #     if boundary == "top":
    #         if self.xcor() > 300 - self.xcor():
    #             return "top_left"
    #         else:
    #             return "top_right"
    #     elif boundary == "bottom":
    #         if self.xcor() > 300 - self.xcor():
    #             return "bottom_left"
    #         else:
    #             return "bottom_right"


    