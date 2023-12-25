import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins=0
    python_wins=0

    def play_rps():
        nonlocal player_wins
        nonlocal player_wins
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

            def decide_winner(player, computer):
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 3:
                    player_wins += 1
                    return "🍾You win!"
                elif player == 2 and computer == 1:
                    player_wins += 1
                    return "🍾You win!"
                elif player == 3 and computer == 2:
                    player_wins += 1
                    return "🍾You win!"
                elif player == computer:
                    return "😲Tie game! "
                else:
                    python_wins += 1
                    return "🐍Python wins!"

            game_result = decide_winner(player, computer)
            print(game_result)

            nonlocal game_count
            game_count += 1
            print("\n Game Count: " + str(game_count))
            print("\nUser wins: " + str(player_wins))
            print("\nPython wins: " + str(python_wins))

            playagain = input("\nPlay again? \Y for yes or \nQ to quit \n\n")
            if playagain.lower() == "y":
                continue
            else:
                print("Thank you for playing 🙏🙏🙏🙏🙏")
                break

    return play_rps

play= rps()
play()
sys.exit("BYE 👋👋")

