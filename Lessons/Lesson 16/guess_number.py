import sys
import random
from enum import Enum


def guessNumber(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal player_wins



        playagain = True
        while playagain:
            print("")
            player_choice = input(f" {name},please enter a number between 1 and 3 \n")
            player = int(player_choice)
            if player < 1 or player > 3:
                sys.exit(f"{name}, please enter, 1,2,or 3")

            computer_choice = random.choice("123")
            computer = int(computer_choice)
            print("")

            print(f"\n{name}, you chose {player}.")
            print(f"\nPython chose {computer}.\n")
            print("")

            def decide_winner(player, computer):
                nonlocal name
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 3:
                    player_wins += 1
                    return f"🍾{name,}you win!"
                elif player == 2 and computer == 1:
                    player_wins += 1
                    return f"🍾{name,}you win!"
                elif player == 3 and computer == 2:
                    player_wins += 1
                    return f"🍾{name,}you win!"
                elif player == computer:
                    return "😲Tie game! "
                else:
                    python_wins += 1
                    return f"🐍Python wins!\n sorry, {name}...😥😥"

            game_result = decide_winner(player, computer)
            print(game_result)

            nonlocal game_count
            game_count += 1
            print(f"\n Game Count:  {game_count}")
            print(f"\n {name}'s wins:  {player_wins}")
            print(f"\n Python Count:  {python_wins}")

            playagain = input(f"\nPlay again, {name}? \Y for yes or \nQ to quit \n\n")
            if playagain.lower() == "y":
                continue
            else:
                print("Thank you for playing 🙏🙏🙏🙏🙏")
                sys.exit("BYE 👋👋")

    return guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalize game experience.'
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet"
    )

    args = parser.parse_args()
    rock_paper_scissors = guessNumber(args.name)
    rock_paper_scissors()
