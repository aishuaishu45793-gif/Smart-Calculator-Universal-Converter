
"""
Input validation utilities.
"""


def get_number(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_choice(message, valid_choices):

    while True:

        choice = input(message).strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice! Please try again.")
