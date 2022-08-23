# ############## BUG - Pressing right of left and immediately pressing forward or backward reverses the snake ##########

from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Xenia")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="space", fun=screen.exitonclick)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # Update Score
        scoreboard.increase_score()
    # Detect collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.snake_head.distance(body) < 10:
            scoreboard.reset()
            snake.reset()



