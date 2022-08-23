from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_paddle.goto(-350, 0)
ball = Ball()
r_scoreboard = Scoreboard((200, 280))
l_scoreboard = Scoreboard((-200, 280))


screen.listen()

screen.onkey(key="Up", fun=r_paddle.move_paddle_up)
screen.onkey(key="Down", fun=r_paddle.move_paddle_down)
screen.onkey(key="w", fun=l_paddle.move_paddle_up)
screen.onkey(key="s", fun=l_paddle.move_paddle_down)

game_on = True

while game_on:
    time.sleep(ball.ball_pace)
    ball.move()
    screen.update()
    # Detect Collision with the top wall
    if ball.collide_wall():
        ball.bounce_vertical()
    # Detect Collision with paddle     || Can't create a collide_paddle() in class Ball because this condition will
    # need access to class Paddle instances where everything regarding wall collision
    # can be implemented through coordinates
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
        ball.bounce_horizontal()
    elif ball.xcor() > 380:
        l_scoreboard.increase_score()
        ball.refresh_ball()
        ball.bounce_horizontal()

    elif ball.xcor() < -380:
        r_scoreboard.increase_score()
        ball.refresh_ball()
        ball.bounce_horizontal()

    if r_scoreboard.score == 10 or l_scoreboard.score == 10:
        game_on = False
        if r_scoreboard.score == 10:
            r_scoreboard.goto(0, 0)
            r_scoreboard.write(f"Game Over. Player on the Right Wins!", align="center", font=("COURIER", 14, "normal"))
        elif l_scoreboard.score == 10:
            l_scoreboard.goto(0, 0)
            l_scoreboard.write(f"Game Over. Player on the Left Wins!", align="center", font=("COURIER", 14, "normal"))


screen.exitonclick()
