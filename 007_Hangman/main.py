#class import

import random


# Hangman stages

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



print(logo)

# Greeting to the user

print("Welcome to Hangman Game!")

# Sample word list
word_list = ["challenge","bee","baboon","camel","race"]

# variables
selected_word = random.choice(word_list)
word_lenght = len(selected_word)
live = len(stages)-1
game_end = False
#for test purpose

print(f"the solution is {selected_word} word.")

# create a empty list

display_word = []

for _ in range(word_lenght):
    display_word += "_"

# try to loop till the user win or lose


while not game_end:
    # ask user for input
    user_input = input("Enter a letter:\n").lower()

    # Show the user the selected word
    if user_input in display_word:
        print(f"Your selected letter is {user_input}")
    # replace underscore with the right letter
    for position in range(word_lenght):
        letter = selected_word[position]
        if letter == user_input:
            display_word[position] = letter



# control if the user is wrong
    if user_input not in selected_word:
        print(f"Your selected letter is {user_input} , but not include in word. One live minus")
        live -=1
        if live == 0:
            game_end = True
            print("You Lose")


    if "_" not in display_word:
        game_end = True
        print("You Win!")
    print(stages[live])
    print(f"{'  '.join(display_word)}")