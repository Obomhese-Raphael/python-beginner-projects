# Loop until user wants to stop playing
# Ask: role the dice?
# If user enters y
# Generate a random number between 1 and 6 and print them
# If user enters n, print "Thanks for playing" and then terminate the program
# Else
# print invalid input and ask the user to enter y or n

import random

total_rolls = 0

while True:
    choice = input("Roll the dice? (y/n): ")
    if choice.lower() == 'y':
        number_to_roll = int(input("How many dice do you want to roll? "))
        if number_to_roll <= 0:
            print("Please enter a number greater than 0.")
            continue
        results = []
        for _ in range(number_to_roll):
            roll = random.randint(1, 6)
            results.append(roll)
        total_rolls += 1
        print(f"You rolled: {results}")
        print(f"Total times rolled this session: {total_rolls}")
    elif choice.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter y or n.")
