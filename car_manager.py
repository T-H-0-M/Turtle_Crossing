from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_POSITIONS = [(280, )]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 # This is how much the move distance will increase with each level.


class CarManager:

    def __init__(self):
        self.cars = []

    def generate_car(self):
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
        for car in self.cars:
            car.goto(car.xcor() - (STARTING_MOVE_DISTANCE + ((level - 1) * MOVE_INCREMENT)), car.ycor())

    def check_collision(self, player):
        for car in self.cars:
            if player.distance(car) <= 20 and player.ycor() == car.ycor():
                return True
        return False

    def reset_level(self):
        self.cars = []

