from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=400, width=500)

user_bet = screen.textinput(title="Make A Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtles = [
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
]
y_postion = -100
count = 0
for t_num in turtles:
    t_num.penup()
    t_num.color(colors[count])
    t_num.goto(x = -240, y = y_postion)
    y_postion +=28
    count +=1

if user_bet:
    start_race = True

while start_race:
    for t in turtles:
        random_distance = random.randint(0, 10)
        t.forward(random_distance)
        if t.xcor() > 230:
            start_race = False
            turtle_color = t.color()[0]
            print(f"The {turtle_color} turtle wins!")
            if turtle_color == user_bet:
                print("You won the bet.")
            else:
                print("You lost the bet.")

            break

# -----------------Event Listeners----------------- 
# def move_backwards():
#     tim.backward(10

# def move_forwards():
#     tim.forward(10)

# def move_clockwise():
#     tim.right(10)

# def move_counter_clockwise():
#     tim.left(10)

# def clear_screen():
#     tim.reset()

# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=move_clockwise, key="d")
# screen.onkey(fun=move_counter_clockwise, key="a")
# screen.onkey(fun=clear_screen, key="c")
# screen.listen()


screen.exitonclick()
