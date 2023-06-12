"""
player.py

This module contains the Player class, which represents the player character in a game.
The player can move up the screen to avoid obstacles and reach the finish line.

Author: Thomas Bandy

"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    The Player class represents the player character in a game.
    The player can move up the screen to avoid obstacles and reach the finish line.

    Inherited Attributes:
        xcor (float): The x-coordinate of the player's position.
        ycor (float): The y-coordinate of the player's position.

    Methods:
        move(): Moves the player up the screen.
        reset_player(): Resets the player's position to the starting position.

    """

    def __init__(self):
        """
        Initializes a Player object.
        The player is represented by a turtle shape and is initially positioned at the starting position.

        """
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """
        Moves the player up the screen by the defined move distance.

        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_player(self):
        """
        Resets the player's position to the starting position.

        """
        self.goto(STARTING_POSITION)
