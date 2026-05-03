
from systemsmanager import SystemsManager

class Menu:

    def greet_user(self):
        print("Hello, which problem are you looking to solve today?")

    def menu(self):
        print("1. Solving system of linear equations")
        print("2. Finding the inverse of a matrix")
        print("3. Quit")


MainMenu = Menu()
manager=SystemsManager()
MainMenu.greet_user()

while True:
    MainMenu.menu()
    try:
        # Try to convert the user's input to an integer
        choice = int(input("Enter your choice: "))

        # Now check that the number is one of the valid options
        if choice == 1:
            manager.solve_linear_system()
        elif choice == 2:
            # We'll fill this in later
            break
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            # The input was a number, but not 1, 2, or 3
            print("Please enter a valid choice.\n")

    except ValueError:
        # Handles cases where user types something that cannot be converted to int
        print("Please enter a valid choice.\n")