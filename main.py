import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars
    cars.create_car()
    # move cars across the game
    cars.move_cars()

    # detect collision with car object
    for car in cars.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.player_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()
