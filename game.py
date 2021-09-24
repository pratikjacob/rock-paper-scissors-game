# game.py

import os
from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default = "Player One")
print(PLAYER_NAME)

import random

print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT
user_choice = input("Choose 'rock' or 'paper' or 'scissors':  ")
if ((user_choice != "rock") and (user_choice != "paper") and ("user_choice" != "scissors")):
    print("You did not select a valid option. Please play again.")
    exit()
else:
    print("YOU CHOSE: " + user_choice)

# COMPUTER CHOICE AT RANDOM

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("COMPUTER CHOSE: " + computer_choice)


#CONDITIONALS TO DETERMINE WINNER

if ((user_choice == "rock") and (computer_choice == "rock")):
    print("TIE")
elif ((user_choice == "paper") and (computer_choice == "paper")):
    print("TIE")
elif ((user_choice == "scissors") and (computer_choice == "scissors")):
    print("TIE")
elif ((user_choice == "rock") and (computer_choice == "paper")):
    print("YOU LOSE")
elif ((user_choice == "rock") and (computer_choice == "scissors")):
    print("YOU WIN")
elif ((user_choice == "paper") and (computer_choice == "rock")):
    print("YOU WIN")
elif ((user_choice == "paper") and (computer_choice == "scissors")):
    print("YOU LOSE")
elif ((user_choice == "scissors") and (computer_choice == "rock")):
    print("YOU LOSE")
elif ((user_choice == "scissors") and (computer_choice == "paper")):
    print("YOU WIN")

#SCORE COUNT
#user_score = 0
#computer_score = 0

#if (((user_choice == "rock") and (computer_choice == "scissors")) or ((user_choice == "paper") and (computer_choice == "rock")) or ((user_choice == "scissors") and (computer_choice == "paper"))):
#    user_score = user_score + 1
#elif (((user_choice == "rock") and (computer_choice == "paper")) or ((user_choice == "paper") and (computer_choice == "scissors")) or ((user_choice == "scissors") and (computer_choice == "rock"))):
#    computer_score = computer_score + 1
#print("YOUR SCORE: " + user_score)
#print("COMPUTER'S SCORE " + computer_score)