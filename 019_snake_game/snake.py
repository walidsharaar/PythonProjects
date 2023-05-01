from turtle import Turtle

STARTING_POSITION =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP= 90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.parts =[]
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_part(position)

    def add_part(self,position):
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.goto(position)
            self.parts.append(part)

    def snake_extend(self):
        self.add_part(self.parts[-1].position())

    def move_snake(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part_num - 1].xcor()
            new_y = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






