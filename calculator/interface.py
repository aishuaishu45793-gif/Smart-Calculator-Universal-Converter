
"""
Calculator Interface
Connects calculator functions with the user.
"""

from calculator import basic, scientific
import calculator.basic as basic
import calculator.scientific as scientific
from utils.validators import get_number, get_choice


def basic_calculator():

    while True:

        print("\n====== BASIC CALCULATOR ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Percentage")
        print("8. Back to Main Menu")

        choice = get_choice(
            "Select operation: ",
            [str(i) for i in range(1, 9)]
        )

        if choice == "8":
            break

        a = get_number("Enter first number: ")

        if choice == "7":
            b = get_number("Enter percentage: ")
        else:
            b = get_number("Enter second number: ")

        try:

            operations = {
                "1": basic.add,
                "2": basic.subtract,
                "3": basic.multiply,
                "4": basic.divide,
                "5": basic.modulus,
                "6": basic.power,
                "7": basic.percentage
            }

            result = operations[choice](a, b)

            print("\nResult:", result)

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print("Calculation error:", error)


def scientific_calculator():

    while True:

        print("\n====== SCIENTIFIC CALCULATOR ======")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Sine")
        print("4. Cosine")
        print("5. Tangent")
        print("6. Logarithm")
        print("7. Natural Logarithm")
        print("8. Back to Main Menu")

        choice = get_choice(
            "Select operation: ",
            [str(i) for i in range(1, 9)]
        )

        if choice == "8":
            break

        number = get_number("Enter a number: ")

        try:

            operations = {
                "1": scientific.square_root,
                "2": scientific.factorial,
                "3": scientific.sine,
                "4": scientific.cosine,
                "5": scientific.tangent,
                "6": scientific.logarithm,
                "7": scientific.natural_log
            }

            result = operations[choice](number)

            print("\nResult:", result)

        except (ValueError, OverflowError) as error:
            print("Calculation error:", error)
