from turtle import Turtle, Screen
class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.skin = "scales"
    
    def swim(self):
        print("Moving in water.")
    
    def breath(self):
        print("Underwater breathing")
        super().breath()
        # return super().breath()

animal = Animal()
print(animal.num_eyes)
animal.breath()
print("_" * 100)
nemo = Fish()
print(nemo.num_eyes)
nemo.swim()
nemo.breath()
print("_" * 100)
print("_" * 100)


s= Screen()
tim = Turtle()
pen = Turtle()
# pen.forward(77)
tim.distance(pen)
tim.pos()

# tim.distance()

print(tim.distance(pen))
s.exitonclick()