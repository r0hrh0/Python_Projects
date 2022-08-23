from turtle import Turtle
steps = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        x = 0
        y = 0
        for size in range(3):
            self.add_snake_body(x, y)
            x -= 20

    def add_snake_body(self, x, y):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.speed("fastest")
        snake.goto(x, y)
        self.snake_body.append(snake)

    def extend(self):
        # print(self.add_snake_body(self.snake_body[-1].xcor())
        self.add_snake_body(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def move(self):
        for snake in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake-1].xcor()
            new_y = self.snake_body[snake-1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.snake_head.forward(steps)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
