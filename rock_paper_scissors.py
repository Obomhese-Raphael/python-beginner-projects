# Rock - Paper - Scissors Game
# The player will choose either rock, paper, or scissors, and the computer will randomly select one of the three options as well.
# The rules of the game are as follows:
# - Rock beats scissors (rock crushes scissors)
# - Scissors beats paper (scissors cut paper)
# - Paper beats rock (paper covers rock)
# The game will determine the winner based on the player's choice and the computer's choice, and it will keep track of the number of wins, losses, and ties for the player.
# The game will continue until the player decides to stop playing.


import random

options = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0
ties = 0

while True:
    player_choice = input(
        "Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
    if player_choice == 'exit':
        print("Thanks for playing!")
        break
    elif player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
        ties += 1
    elif player_choice == "rock" and computer_choice == "scissors":
        print(f"You chose rock and the computer chose scissors.")
        print("Rock crushes scissors. You win!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print(f"You chose scissors and the computer chose paper.")
        print("Scissors cut paper. You win!")
        player_wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print(f"You chose paper and the computer chose rock.")
        print("Paper covers rock. You win!")
        player_wins += 1
    else:
        print(f"You chose {player_choice} and the computer chose {computer_choice}.")
        print(f"{computer_choice.capitalize()} beats {player_choice}. You lose!")
        computer_wins += 1
    print(f"Score: You {player_wins} - Computer {computer_wins} - Ties {ties}")

