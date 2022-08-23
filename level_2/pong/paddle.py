from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_paddle_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def move_paddle_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)



