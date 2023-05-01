from random import randint
from art import  logo

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5


#function to check user guess number with computer generated number

def check(answer , guess ,turns):
    """Check answer compare to guess and return remaining turns"""

    if guess<answer:
        print(f"{answer} is too high compared to guess number.")
        return turns -1
    elif guess>answer:
        print(f"{answer} is too low compared to guess number.")
        return turns -1
    else:
        print(f"You got it ! the answer was {answer} .")

#function to ask the difficulties

def difficuly():
    level = input("Choose the difficulty level: Type 'Easy' or 'Hard'   ").lower()
    if level == 'easy':
        return EASY_ATTEMPT
    elif level=='hard':
        return HARD_ATTEMPT
    else:
        print("Invalid Input !")
        return 0


def play_game():

    print(logo)
    print("Welcome to Guessing Game")
    print("Think a number between 1 to 100! ")

    #pick the number between 1 to 100

    answer = randint(1,100)
    print(f"Computer guess number is {answer}")

    turns = difficuly()
    guess =0
    while guess !=answer:
        print(f"You have {turns} attempts. ")
        #store the guess number
        guess = int(input("What is your guess: "))

        # check number of turns and substract by 1 in each wrong guess

        turns = check(guess,answer,turns)
        if turns == 0 :
            print("You can't guess more. You lose.")
            return
        elif guess !=answer :
            print("Guess once again. ")



# call the start function

play_game()






