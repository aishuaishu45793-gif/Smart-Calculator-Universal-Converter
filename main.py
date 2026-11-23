
"""
SMART CALCULATOR & UNIVERSAL CONVERTER
Main Application File

Version: 1.0.0
"""

from config import APP_NAME, APP_VERSION, AUTHOR

# Import calculator modules
from calculator.interface import (
    basic_calculator,
    scientific_calculator
)

# Import converter module
from converters.interface import unit_converter


# --------------------------------------------------
# 1. APPLICATION BANNER
# --------------------------------------------------

def display_banner():
    print("\n" + "=" * 60)
    print(f"       {APP_NAME}")
    print(f"                 Version {APP_VERSION}")
    print("=" * 60)
    print("Welcome to your Smart Calculator & Universal Converter!")


# --------------------------------------------------
# 2. MAIN MENU
# --------------------------------------------------

def display_menu():
    print("\n============== MAIN MENU ==============")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Unit Converter")
    print("4. Currency Converter")
    print("5. View Calculation History")
    print("6. Export History to CSV")
    print("7. Manage Favorites")
    print("8. About Project")
    print("9. Exit")
    print("=" * 39)


# --------------------------------------------------
# 3. CURRENCY CONVERTER
# --------------------------------------------------

def currency_converter():
    print("\n========== CURRENCY CONVERTER ==========")
    print("Currency converter will be implemented in Phase 4.")
    print("It will support online exchange rates.")


# --------------------------------------------------
# 4. CALCULATION HISTORY
# --------------------------------------------------

def view_history():
    print("\n========== CALCULATION HISTORY ==========")
    print("Calculation history will be implemented in a later phase.")


# --------------------------------------------------
# 5. EXPORT HISTORY
# --------------------------------------------------

def export_history():
    print("\n========== EXPORT HISTORY ==========")
    print("CSV export will be implemented in a later phase.")


# --------------------------------------------------
# 6. FAVORITES
# --------------------------------------------------

def manage_favorites():
    print("\n========== FAVORITES ==========")
    print("Favorites will be implemented in a later phase.")


# --------------------------------------------------
# 7. ABOUT PROJECT
# --------------------------------------------------

def about_project():
    print("\n========== ABOUT PROJECT ==========")

    print(f"Project Name : {APP_NAME}")
    print(f"Version      : {APP_VERSION}")
    print(f"Developer    : {AUTHOR}")

    print("\nPROJECT FEATURES:")
    print("1. Basic arithmetic calculations")
    print("2. Scientific calculations")
    print("3. Length conversion")
    print("4. Weight conversion")
    print("5. Temperature conversion")
    print("6. Online currency conversion (planned)")
    print("7. Calculation history (planned)")
    print("8. CSV export (planned)")
    print("9. Favorites management (planned)")

    print("\nDeveloped using Python.")


# --------------------------------------------------
# 8. MAIN APPLICATION
# --------------------------------------------------

def main():

    display_banner()

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":

            basic_calculator()

        elif choice == "2":

            scientific_calculator()

        elif choice == "3":

            unit_converter()

        elif choice == "4":

            currency_converter()

        elif choice == "5":

            view_history()

        elif choice == "6":

            export_history()

        elif choice == "7":

            manage_favorites()

        elif choice == "8":

            about_project()

        elif choice == "9":

            print("\n" + "=" * 45)
            print("Thank you for using Smart Calculator!")
            print("Goodbye!")
            print("=" * 45)

            break

        else:

            print("\nInvalid choice!")
            print("Please enter a number between 1 and 9.")


# --------------------------------------------------
# 9. PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()
