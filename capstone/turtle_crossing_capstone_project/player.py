from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor()+10)

    def at_finish_line(self):
        return self.ycor() > 280

    def refresh(self):
        self.goto(STARTING_POSITION)
