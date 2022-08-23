from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_pace = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collide_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1
    # def bounce_from_left(self):
    #     self.x_move *= (abs(self.x_move))
    #     self.ball_pace *= 0.9
    #
    # def bounce_from_right(self):
    #     self.x_move *= -(abs(self.x_move))
    #     self.ball_pace *= 0.9

    def refresh_ball(self):
        self.ball_pace = 0.03
        start_y = random.randint(-280, 280)
        self.setposition(0, start_y)

