import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for cars in car_manager.car_list:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.at_finish_line():
        scoreboard.increase_score()
        car_manager.speed_up_car()
        player.refresh()


screen.exitonclick()
