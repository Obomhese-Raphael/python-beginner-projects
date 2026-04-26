# Random Password Generator
# This script generates a random password based on user-defined criteria such as length and character types.
# Author: OpenAI's ChatGPT
# Date: 2024-06

import random
import string


def generate_password(length, use_digits=True, use_uppercase=True, use_lowercase=True, use_special_chars=True):
    """Generates a random password based on the specified criteria."""
    characters = ""

    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Random Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_uppercase = input(
            "Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input(
            "Include lowercase letters? (y/n): ").lower() == 'y'
        use_special_chars = input(
            "Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(
            length, use_digits, use_uppercase, use_lowercase, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
