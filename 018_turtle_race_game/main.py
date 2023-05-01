import random
import turtle
from turtle import  Turtle,Screen

is_race_on =False
screen = Screen()
screen.setup(width=600 , height= 500)
color_list=["red","blue","green","yellow","purple","orange"]
positions = [-70 , -40 , -10,20,50,80]
guess = screen.textinput(title="Turtles Racing Game",prompt="Which turtle color will will the race?   ")
raced_turtle =[]
for turtle_index in range(0,6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(color_list[turtle_index])
    my_turtle.goto(x=-280, y =positions[turtle_index])
    raced_turtle.append(my_turtle)


if guess:
    is_race_on= True

while is_race_on:
    for turtle in raced_turtle:
        if turtle.xcor()>280:
            is_race_on=False
            winner = turtle.pencolor()
            if winner == guess:
                print(f"You won {winner} is the winner!")
            else:
                print(f"You lost {winner} is the winner!")


        distance= random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()