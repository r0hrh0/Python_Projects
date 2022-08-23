from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

# ###############How_Higher_Order_Functions_Work##################################################################
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# def move_count_clk():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def move_clk():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=move_clk)
# screen.onkey(key="a", fun=move_count_clk)
# screen.onkey(key="c", fun=clear)
###############################################################################################################

# #################################Turtle Race#################################################################


def on_your_marks():
    color_list = ["red", "blue", "green", "black", "yellow", "brown", "pink"]
    no_of_turtles = len(color_list)
    turtle_list = []
    for turtles in range(no_of_turtles):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color_list[turtles])
        turtle_list.append(new_turtle)
    return turtle_list


def bet_set():
    bet = screen.textinput(title="Make Bet", prompt="Which turtle do you want ot bet on? \n Red/Blue/Black/Yellow/Brown/Pink/Green: ")
    print(bet)
    return bet


def start_race():
    turtle_list = on_your_marks()
    x = -230
    y = -200
    for turtles in turtle_list:
        y += 50
        turtles.penup()
        turtles.goto(x, y)
    bet = bet_set()
    if bet:
        racing = True
    while racing:
        for turtles in turtle_list:
            if turtles.xcor() >= 230:
                racing = False
                winning_color = turtles.pencolor()
                if winning_color == bet:
                    print(f"You've won the bet! The {bet} turtle has won!")
                else:
                    print(f"You've lost the bet! The {winning_color} turtle has won!")
            random_distance = random.randint(1, 10)
            turtles.forward(random_distance)


start_race()

screen.exitonclick()
