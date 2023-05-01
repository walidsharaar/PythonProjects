# Project start
import random

print("Welcome to Rock Paper Scissor Game ! \n")

# variable definition

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_emojis=[rock,paper,scissors]


user_selection = int(input("Choose 1 for Rock, 2 for Paper or 3 for Scissors:\n"))

computer_selection= random.randint(1,3)

print("Computer Choice is : ")
print(game_emojis[computer_selection])

if user_selection >=4 or user_selection <1:
    print("You typed invalid number,you lose!")
elif user_selection==1 and computer_selection == 3:
    print("You Win!!")
elif user_selection ==3 and computer_selection==1:
    print("You Lose!")
elif user_selection > computer_selection:
    print("You Win!")
elif computer_selection>user_selection:
    print("You Lose!")
elif computer_selection == user_selection :
    print("its is a draw")


