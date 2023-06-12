"""
main.py

This module contains the main logic for a game where the player controls a character to avoid cars
and reach the finish line. The game uses the Turtle module for graphics and includes classes such
as Player, CarManager, and Scoreboard for managing player movement, car generation and movement,
and scorekeeping, respectively.

Author: Thomas Bandy

"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Setting up player, car_manager, scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen event listener
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_over = False
count = 6
while not game_over:
    time.sleep(0.1)
    car_manager.move(scoreboard.level)
    car_manager.generate_car()
    screen.update()

    # Player collision with cars
    if car_manager.check_collision(player):
        game_over = True
        scoreboard.gameover()

    # Player reaching finish line
    if player.ycor() >= 280:
        scoreboard.increment_level()
        player.reset_player()

screen.exitonclick()
