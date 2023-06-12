"""
car_manager.py

This module contains the CarManager class, which manages the generation, movement, collision detection,
and resetting of cars in a game.

Author: Thomas Bandy

"""

from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_POSITIONS = [(280,)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # This is how much the move distance will increase with each level.


class CarManager:
    """
    The CarManager class is responsible for managing the generation, movement, collision detection,
    and resetting of cars in a game.

    Attributes:
        cars (list): A list of Turtle objects representing the cars in the game.

    Methods:
        generate_car(): Generates a car approximately every 6 calls.
        move(level): Moves the cars based on the level, increasing the move distance each time.
        check_collision(player): Checks if the player collides with any of the cars.
        reset_level(): Resets the cars list.

    """

    def __init__(self):
        """
        Initializes a CarManager object with an empty list of cars.

        """
        self.cars = []

    def generate_car(self):
        """
        Generates a car approximately every 6 calls.
        The car is created with a random position, color, and size.

        """
        if random.randint(1, 6) == 6:
            start_x = random.randrange(300, 400, 5)
            start_y = random.randrange(-250, 250, 10)
            temp = Turtle()
            temp.penup()
            temp.shape("square")
            temp.color(random.choice(COLOURS))
            temp.shapesize(stretch_len=2, stretch_wid=1)
            temp.goto(start_x, start_y)
            self.cars.append(temp)

    def move(self, level):
        """
        Moves each car in the cars list based on the current level.
        The move distance is increased with each level.

        Args:
            level (int): The current level of the game.

        """
        for car in self.cars:
            car.goto(
                car.xcor() - (STARTING_MOVE_DISTANCE + ((level - 1) * MOVE_INCREMENT)),
                car.ycor(),
            )

    def check_collision(self, player):
        """
        Checks if the player collides with any of the cars.

        Args:
            player (Turtle): The Turtle object representing the player.

        Returns:
            bool: True if the player collides with a car, False otherwise.

        """
        for car in self.cars:
            if player.distance(car) <= 20 and player.ycor() == car.ycor():
                return True
        return False

    def reset_level(self):
        """
        Resets the list of cars, removing all existing cars.

        """
        self.cars = []
