import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

player=Player()
car=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    for i in car.turtles:
        if player.distance(i)<20:
            game_is_on=False
            score.game_over()

    if player.ycor()>=280:
        car.increase_speed()
        player.next_level()
        score.increase_level()


screen.exitonclick()