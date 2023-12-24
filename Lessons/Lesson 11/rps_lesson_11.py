import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playagain = True
    while playagain:
        print("")
        player_choice = input("Enter... \n1 for Rock, "
                              "\n2 for Paper, \n3 for Scissors:\n\n")
        player = int(player_choice)
        if player < 1 or player > 3:
            sys.exit("You have entered an invalid value, 1,2,or 3")

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        print("")
        print("You chose: " + str(RPS(player)).replace('RPS.', ".") + ".")
        print("Python chose: " + str(RPS(computer)).replace('RPS.', ".") + ".")
        print("")
        def decide_winner(player,computer):
            if player == 1 and computer == 3:
                return "🍾You win!"
            elif player == 2 and computer == 1:
                return "🍾You win!"
            elif player == 3 and computer == 2:
                return "🍾You win!"
            elif player == computer:
                return "😲Tie game! "
            else:
                return "🐍Python wins!"
        game_result= decide_winner(player,computer)
        print(game_result)


        global game_count
        game_count += 1
        print("\n Game Count: "+str(game_count))

        playagain = input("\nPlay again? \Y for yes or \nQ to quit \n\n")
        if playagain.lower() == "y":
            continue
        else:
            print("Thank you for playing 🙏🙏🙏🙏🙏")
            break


play_rps()
sys.exit("BYE 👋👋")
