import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.fillcolor("black")
# flag = 10
# while flag:
#      tim.pendown()
#      tim.forward(5)
#      tim.penup()
#      tim.forward(5)
#      flag -= 1

# tim.penup()
# tim.setpos(-80, 200)
# tim.pendown()


# def draw_shapes(no_of_sides):
#     angle = 360 / no_of_sides
#     for side in range(no_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for sides in range(3, 7):
#     tim.color(random.choice(colors))
#     draw_shapes(sides)

# end of drawing shapes

# beg of random walk


distance = [30]
angle = [0, 90, 180, 270]


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk():
    tim.pensize(10)
    tim.speed("fastest")

    for times in range(0, 500):
        color = random_colors()
        tim.color(color)
        tim.forward(random.choice(distance))
        tim.setheading(random.choice(angle))


# random_walk()

def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for circles in range(int(360/size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading+size_of_gap)


draw_spirograph(1)

screen.exitonclick()
