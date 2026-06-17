from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POS = 300


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1
        self.max_speed = 0.00009
    
    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            y_random = random.randint(-250,250)
            new_car.goto(X_POS, y_random)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        if self.car_speed >= self.max_speed:
            self.car_speed *= 0.5
  

