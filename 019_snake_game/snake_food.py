import random
from turtle import  Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=-0.6 ,stretch_wid=0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        random_xplace = random.randint(-270, 270)
        random_yplace = random.randint(-270, 270)
        self.goto(random_xplace, random_yplace)

