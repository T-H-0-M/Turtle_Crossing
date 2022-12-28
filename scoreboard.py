from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-235, 260)
        self.level = 1
        self.write_level()

    def increment_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    # Generate finish line
