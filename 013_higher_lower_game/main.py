from data import data
import random
from art import logo, vs
#todo get data from random account

def get_different_account():
    """Get data from random account"""
    return random.choice(data)

# todo format the account data
def format_data(account):
    """formating the dictionary data into printable format."""
    name = account["name"]
    description= account["description"]
    country= account["country"]
    return(f"{name}, a {description} , from {country}")


def check_answer(guess,first_account_follower,second_account_follower):
    """if statement usage to check the correct answer"""
    if first_account_follower > second_account_follower:
        return guess=="a"
    else:
        return guess =="b"


def play_game():
    print(logo)
    score= 0
    game_continue = True
    #todo display art
    print(logo)
    # todo generate random from the list of data
    first_account= get_different_account()
    second_account= get_different_account()
#todo loop the game until getting wrong answer
    while game_continue:
        first_account = second_account
        second_account = get_different_account()
#todo loop to generate different account
        while first_account == second_account:
        # ensure two accounts are different
            second_account=random.choice()

        print(f"Compare A : {format_data(first_account)}")
        print(vs)
        print(f"Compare B : {format_data(second_account)}")

        #todo ask user guess

        guess = input("Who has the more followers? A or B  ").lower()
        first_account_follower = first_account["follower_count"]
        second_account_follower = second_account["follower_count"]

        # todo check the user guess
        is_right = check_answer(guess,first_account_follower,second_account_follower)
        print(logo)
        if is_right:
            score +=1
            print(f"You guess right! your score is {score}")
        else:
            game_continue=False
            print(f"Sorry you are wrong. Your score is : {score}")


play_game()