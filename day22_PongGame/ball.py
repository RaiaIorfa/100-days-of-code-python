from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)