# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# screen.listen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def speed():
#     tim.speed("fastest")
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.onkey(speed, "s")
# screen.exitonclick()
import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color : ")
colors = ["Red", "Indigo", "Blue", "Green", "Orange", "Yellow", "Red"]
y_positions = [-70, -40, -10, 20, 50, 80, 110, 140, 170]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)



if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've loose! The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()