from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1

    def increment_level(self):
        self.level += 1

    def write_level(self):
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

