from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.turtles=[]
        self.starting_speed=STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1,6)==1:
            new_car=Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-200, 200))
            self.turtles.append(new_car)

    def move_cars(self):
        for i in self.turtles:
            i.bk(self.starting_speed)
    def increase_speed(self):
        self.starting_speed+=MOVE_INCREMENT
