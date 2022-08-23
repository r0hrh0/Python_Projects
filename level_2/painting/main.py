# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
import random
from turtle import Turtle, Screen


color_list = [(223, 73, 55), (233, 144, 82), (19, 14, 14), (44, 88, 149), (231, 245, 238), (150, 66, 86), (214, 231, 238), (228, 221, 102), (124, 170, 200), (121, 167, 130), (19, 138, 87), (243, 223, 7), (83, 173, 90), (39, 44, 68), (89, 33, 35), (230, 172, 180), (222, 61, 92), (195, 128, 158), (115, 65, 45), (78, 48, 84), (16, 164, 214), (174, 187, 45), (161, 209, 185), (146, 209, 234)]
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.resizemode("user")
tim.shapesize(0.6, 0.6, 0)
tim.shape("circle")
tim.color("black")
tim.penup()
tim.speed("fastest")
tim.setpos(-300, -250)


# def travel_using_coordinates(x, y, colour_list):
#     x_cord = x
#     y_cord = y
#     for times in range(10):
#         while x_cord <= 150:
#             dot_color = random.choice(colour_list)
#             tim.dot(20, dot_color)
#             tim.forward(50)
#             x_cord += 50
#         x_cord = x
#         y_cord = y_cord+50
#         tim.setpos(x_cord, y_cord)
#         times -= 1
#     tim.hideturtle()
#

def travel_using_dot_number(dot_number, color_list):

    for dot in range(1, dot_number+1):
        colour = random.choice(color_list)
        tim.dot(20, colour)
        tim.forward(50)
        if dot % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)



# travel_using_coordinates(-300, -250, color_list)


travel_using_dot_number(100, color_list)


screen.exitonclick()
