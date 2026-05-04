import re
from gaussian_method_operator import GaussSolver
class SystemsManager:

    # The brain of the program. Handles the actual math operations:
    # solving systems of linear equations and finding matrix inverses.

    def __init__(self):
        # We'll store the matrix size here once the user provides it.
        # For now, it's None because we don't know it yet.
        self.size = None
        self.augmented_matrix = []

    def get_size(self):
        # Ask the user for the size of the system (must be 3 or 4).

        while True:
            try:
                n = int(input("Enter the number of variables in your equations (3 or 4): "))
                if n == 3 or n == 4:
                    self.size = n
                    return  # we got a valid size, exit the loop
                else:
                    print("Size must be exactly 3 or 4.\n")
            except ValueError:
                print("Please enter a valid integer.\n")


    def parse_equation(self, text):

        # Parse an equation string like '3x + 5y - 6z = 8' into a list of
        # coefficients and a constant: [3, 5, -6, 8].
        # Decide which variables to look for based on n

        if self.size == 3:
            variables = ['x', 'y', 'z']
        else:  # size == 4
            variables = ['x', 'y', 'z', 'w']

        # Remove all spaces so '3x + 5y' and '3x+5y' behave the same
        text = text.replace(" ", "").lower()

        # The equation must contain exactly one '=' sign
        if text.count("=") != 1:
            print(" Equation must contain exactly one '=' sign.")
            return None

        # Split into left side (the terms) and right side (the constant)
        left, right = text.split("=")

        # The right side should be a number
        try:
            constant = float(right)
        except ValueError:
            print(f" The right side of '=' must be a number, got '{right}'.")
            return None

        # Now we extract each variable's coefficient from the left side.
        # We'll store them in a dictionary so order doesn't matter.
        coefficients = {}

        for var in variables:
            # Built a regex pattern that finds this variable's coefficient.
            # Examples it should match: '3x', '-3x', '+3x', 'x', '-x', '+x', '1.5x'
            # The pattern: optional sign, optional number, then the variable letter
            pattern = r'([+-]?\d*\.?\d*)' + var
            match = re.search(pattern, left)

            if match is None:
                print(f" Couldn't find variable '{var}' in the equation.")
                return None

            coeff_str = match.group(1)

            # Handle implicit coefficients: 'x' means 1, '-x' means -1
            if coeff_str in ("", "+"):
                coeff = 1.0
            elif coeff_str == "-":
                coeff = -1.0
            else:
                try:
                    coeff = float(coeff_str)
                except ValueError:
                    print(f" Couldn't parse coefficient '{coeff_str}' for {var}.")
                    return None

            coefficients[var] = coeff

        # Build the row in the right order: x, y, z, [w], constant
        row = [coefficients[var] for var in variables]
        row.append(constant)
        return row


    def read_equation_row(self, row_number):

        # Reads one equation from the user as an equation string
        # (e.g., '3x + 5y - 6z = 8') and return it as a list of numbers.
        # Keeps asking until the user gives a valid equation.

        while True:
            raw = input(f"Equation {row_number}: ").strip()

            if raw == "":
                print("You didn't enter anything. Please try again.")
                continue

            # Try to parse the equation
            row = self.parse_equation(raw)

            # parse_equation returns None if something went wrong;
            if row is not None:
                return row

    def read_all_equations(self):
        if self.size == 3:
            example = "3x + 5y - 6z = 8"
        else:
            example = "3x + 5y - 6z + 2w = 8"

        print(f"\n--- Input Mode: Enter equations using x, y, z"
              f"{', w' if self.size == 4 else ''} ---")
        print(f"    Example: {example}\n")

        self.augmented = []
        # Loop n times, reading one equation per iteration
        for i in range(self.size):
            # range(self.size) gives 0, 1, 2, ... but we usually count from 1,
            # so we display i + 1 to the user
            row = self.read_equation_row(i + 1)
            self.augmented.append(row)

    def display_matrix(self):

        # Print the current augmented matrix in a readable format.
        # Shows row numbers so the user knows which row to edit if needed.

        print("\nHere's the augmented matrix [A | b] we built from your equations:\n")
        for i, row in enumerate(self.augmented):
            # Separate the coefficients from the constant with a vertical bar
            coeffs = row[:-1]  # everything except the last element
            constant = row[-1]  # the last element

            # Format each number to 2 decimal places, padded to width 7
            coeff_str = "  ".join(f"{value:7.2f}" for value in coeffs)
            print(f"  Row {i + 1}:  [ {coeff_str}  |  {constant:7.2f} ]")
        print()

    def confirm_or_edit(self):

        # Show the matrix and ask the user if it looks right.
        # If not, let them re-enter individual rows until they're satisfied.

        while True:
            self.display_matrix()
            answer = input("Is this correct? (yes to continue, no to edit a row): ").strip().lower()

            if answer == "yes":
                return  # input is good; we can continue with solving the matrix
            elif answer == "no":
                # Ask which row needs fixing
                self.edit_row()
            else:
                print(" Please answer Yes or No.")

    def edit_row(self):

        # Ask the user which row to edit, then re-read just that row.

        while True:
            try:
                row_num = int(input(f"Which row do you want to fix? (1 to {self.size}): "))
                if 1 <= row_num <= self.size:
                    # Re-read that row using our existing method
                    new_row = self.read_equation_row(row_num)
                    # Replace the bad row in our matrix
                    # row_num is 1-based, but list indexes are 0-based
                    self.augmented[row_num - 1] = new_row
                    return
                else:
                    print(f" Row number must be between 1 and {self.size}.")
            except ValueError:
                print("  ! Please enter a valid row number.")

    def display_solution(self, solution):
        # Display the solution vector with proper variable names.
        # For n=3: shows x, y, z.
        # For n=4: shows x, y, z, w.

        # Pick the right variable names based on the size
        if self.size == 3:
            variables = ['x', 'y', 'z']
        else:  # size == 4
            variables = ['x', 'y', 'z', 'w']

        print("\nSolution:")
        # zip pairs each variable name with its corresponding value
        # so we can iterate over them together
        for var, value in zip(variables, solution):
            # Use format_number to show whole numbers without decimals
            formatted = value
            print(f"  {var} = {formatted}")

    def solve_linear_system(self):

        self.read_all_equations()
        self.confirm_or_edit()

        # calls methods in GaussSolver class
        solver = GaussSolver(self.augmented, self.size)
        solver.solve()

        if solver.is_singular:
            print("\nThe system has no unique solution.")
        else:
            # Will display solver.solution nicely once it's computed
            self.display_solution(solver.solution)
