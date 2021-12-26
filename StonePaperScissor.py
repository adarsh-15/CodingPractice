# from random import choice
from random import randint

num = randint(0, 2)
if num == 1:
    player1 = "Stone"
elif num == 1:
    player1 = "Paper"
else:
    player1 = "Scissor"

player2 = input("Enter you choice for play: ")

if player1 == "Stone" and player2 == "Paper":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player2: Won")
elif player1 == "Paper" and player2 == "Scissor":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player2: Won")
elif player1 == "Scissor" and player2 == "Stone":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player2: Won")
elif player1 == "Scissor" and player2 == "Paper":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player1: Won")
elif player1 == "Paper" and player2 == "Stone":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player1: Won")
elif player1 == "Stone" and player2 == "Scissor":
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Player1: Won")
else:
    print("Player1: ", player1)
    print("Player2: ", player2)
    print("Draw")
