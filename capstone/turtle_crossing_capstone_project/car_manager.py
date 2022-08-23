from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.goto(320, 0)

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            start_y = random.randint(-250, 280)
            position = (320, start_y)
            new_car.goto(position)
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def speed_up_car(self):
        self.car_speed += MOVE_INCREMENT
