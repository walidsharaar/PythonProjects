import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image= "states.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:

    #askk the user
    answer= screen.textinput(title=f" {len(guessed_states)} State Name ",prompt="Enter a state name: ").title()
    if answer == "Exit":
        # missing_states=[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #list comprehension
        missing_states = [state for state in all_states if state not in guessed_states ]
        new_data = pandas.DataFrame(missing_states)
        # Generate the CSV file and the wrong states names.
        new_data.to_csv("States_to_memorize.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_data= data[data.state == answer]
        my_turtle.goto(int(state_data.x),int(state_data.y))
        my_turtle.write(answer)








