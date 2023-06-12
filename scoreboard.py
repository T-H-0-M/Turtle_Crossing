"""
scoreboard.py

This module contains the Scoreboard class, which displays the current level and game over message in a game.

Author: Thomas Bandy

"""

from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    """
    The Scoreboard class displays the current level and game over message in a game.

    Inherited Attributes:
        xcor (float): The x-coordinate of the scoreboard's position.
        ycor (float): The y-coordinate of the scoreboard's position.

    Attributes:
        level (int): The current level.

    Methods:
        increment_level(): Increments the level by 1 and updates the displayed level.
        write_level(): Writes the current level on the scoreboard.
        gameover(): Displays the "GAME OVER" message on the scoreboard.

    """

    def __init__(self):
        """
        Initializes a Scoreboard object.
        The scoreboard is initially positioned and displays the starting level.

        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-235, 260)
        self.level = 1
        self.write_level()

    def increment_level(self):
        """
        Increments the level by 1 and updates the displayed level.

        """
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        """
        Writes the current level on the scoreboard.

        """
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def gameover(self):
        """
        Displays the "GAME OVER" message on the scoreboard.

        """
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
