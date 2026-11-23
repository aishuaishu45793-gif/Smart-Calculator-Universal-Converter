
"""
Interactive Unit Converter
"""

import converters.length as length
import converters.weight as weight
import converters.temperature as temperature

from utils.validators import get_number, get_choice


def unit_converter():

    while True:
        print("\n========== UNIT CONVERTER ==========")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Back to Main Menu")

        choice = get_choice(
            "Select category: ",
            ["1", "2", "3", "4"]
        )

        if choice == "4":
            break

        try:

            # LENGTH CONVERSION
            if choice == "1":

                print("\n------ LENGTH CONVERSION ------")
                print("1. Kilometers to Miles")
                print("2. Miles to Kilometers")
                print("3. Meters to Feet")
                print("4. Feet to Meters")
                print("5. Centimeters to Inches")
                print("6. Inches to Centimeters")

                operation = get_choice(
                    "Select conversion: ",
                    ["1", "2", "3", "4", "5", "6"]
                )

                value = get_number("Enter value: ")

                operations = {
                    "1": (length.km_to_miles, "miles"),
                    "2": (length.miles_to_km, "kilometers"),
                    "3": (length.meters_to_feet, "feet"),
                    "4": (length.feet_to_meters, "meters"),
                    "5": (length.cm_to_inches, "inches"),
                    "6": (length.inches_to_cm, "centimeters")
                }

            # WEIGHT CONVERSION
            elif choice == "2":

                print("\n------ WEIGHT CONVERSION ------")
                print("1. Kilograms to Pounds")
                print("2. Pounds to Kilograms")
                print("3. Grams to Kilograms")
                print("4. Kilograms to Grams")

                operation = get_choice(
                    "Select conversion: ",
                    ["1", "2", "3", "4"]
                )

                value = get_number("Enter value: ")

                operations = {
                    "1": (weight.kg_to_pounds, "pounds"),
                    "2": (weight.pounds_to_kg, "kilograms"),
                    "3": (weight.grams_to_kg, "kilograms"),
                    "4": (weight.kg_to_grams, "grams")
                }

            # TEMPERATURE CONVERSION
            elif choice == "3":

                print("\n------ TEMPERATURE CONVERSION ------")
                print("1. Celsius to Fahrenheit")
                print("2. Fahrenheit to Celsius")
                print("3. Celsius to Kelvin")
                print("4. Kelvin to Celsius")

                operation = get_choice(
                    "Select conversion: ",
                    ["1", "2", "3", "4"]
                )

                value = get_number("Enter temperature: ")

                operations = {
                    "1": (
                        temperature.celsius_to_fahrenheit,
                        "Fahrenheit"
                    ),
                    "2": (
                        temperature.fahrenheit_to_celsius,
                        "Celsius"
                    ),
                    "3": (
                        temperature.celsius_to_kelvin,
                        "Kelvin"
                    ),
                    "4": (
                        temperature.kelvin_to_celsius,
                        "Celsius"
                    )
                }

            function, unit = operations[operation]

            result = function(value)

            print("\n========== RESULT ==========")
            print(f"Original Value: {value}")
            print(f"Converted Value: {result:.4f} {unit}")
            print("============================")

        except ValueError as error:
            print("\nConversion Error:", error)
