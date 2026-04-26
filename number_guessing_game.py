# Number Guessing Game
# The computer will randomly select a number between 1 and 100, and the player will try to guess it.
# The computer will provide feedback on whether the player's guess is too low, too high, or correct.
# The game continues until the player guesses the correct number, and the computer will keep track of the number of attempts it takes for the player to guess the number.


import random

computer_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        player_guess = int(input("Guess a number between 1 and 100: "))
       # 1. Filter out the "illegal" numbers first
        if player_guess > 100 or player_guess < 1:
            print("Please enter a number between 1 and 100.")
            continue  # Skip the rest and restart the loop

        # 2. Now that we know it's a valid guess, count the attempt
        attempts += 1

        # 3. Compare the valid guess to the computer's number
        if player_guess < computer_number:
            print("Too low! Try again.")
        elif player_guess > computer_number:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed {computer_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
