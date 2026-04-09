import random
from turtle import Turtle, Screen

timmy_the_tutle = Turtle()
timmy_the_tutle.shape("arrow")
timmy_the_tutle.color("red")
timmy_the_tutle.penup()

for _ in range(40):
    timmy_the_tutle.forward(100)
    timmy_the_tutle.left(90)
    if _ == 3:
        break



import turtle as t

tim = t.Turtle()
print(tim)

import heroes

print(heroes.gen())
screen = Screen()
screen.exitonclick()



import turtle as t
import random

tim = t.Turtle()

for _ in range(3):
    tim.forward(100)
    tim.left(120)

for _ in range(4):
    tim.forward(100)
    tim.left(90)

for _ in range(5):
    tim.forward(100)
    tim.left(72)

for _ in range(6):
    tim.forward(100)
    tim.left(60)

for _ in range(7):
    tim.forward(100)
    tim.left(51.4)

for _ in range(8):
    tim.forward(100)
    tim.left(45)



import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)
for sides in range(3, 155):
    tim.color(random.choice(colours))
    draw_shape(sides)


RANDOM LINE MOVING TO MAKE LIKE BOX

import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()
directions = [0, 90, 180, 270]
tim.pensize(2)
tim.speed("fastest")

for _ in range(20000):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


DRAW A SPIROGRAPH

from turtle import Turtle, Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)
        tim.circle(70)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()