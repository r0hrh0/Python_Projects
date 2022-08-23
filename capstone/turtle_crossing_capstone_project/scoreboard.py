from turtle import Turtle

FONT = ("Courier", 16, "bold")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 260)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="center", font=FONT)
