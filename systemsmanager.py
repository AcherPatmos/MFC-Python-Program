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
                n = int(input("Enter the size of the system (3 or 4): "))
                if n == 3 or n == 4:
                    self.size = n
                    return  # we got a valid size, exit the loop
                else:
                    print("Size must be exactly 3 or 4.\n")
            except ValueError:
                print("Please enter a valid integer.\n")

    def read_equation_row(self, row_number):

        # Reads one equation from the user and return it as a list of numbers.
        # The list has length self.size + 1 (n coefficients + 1 constant).
        # The user needs to enter n + 1 numbers per row

        expected_count = self.size + 1

        while True:
            # Prompts the user; show them which equation we're on
            raw = input(f"Equation {row_number}: ").strip()

            # Catch the case where they just pressed Enter
            if raw == "":
                print(" You didn't enter anything. Please try again.")
                continue

            # Splits the input on whitespace into a list of strings.
            # "2 1 -1 8".split() gives ["2", "1", "-1", "8"]
            parts = raw.split()

            # Checks if we got the right count BEFORE trying to convert
            if len(parts) != expected_count:
                print(f" Expected {expected_count} numbers, got {len(parts)}. Try again.")
                continue

            # Now tries to convert each piece to a float ( in case decimals appear in the solution).
            # We use try/except in case any piece isn't a valid number.
            try:
                row = [float(p) for p in parts]
                return row  # success — give the row back to the caller
            except ValueError:
                print(" One of those wasn't a valid number. Try again.")

    def read_all_equations(self):
        # showing an example of what the user should input
        if self.size == 3:
            example = "2 1 -1 8"
        else:  # size == 4
            example = "2 1 -1 3 8"

        print(f"\n Input Mode: Enter {self.size + 1} numbers per row (e.g., {example}) ")

        # Reset the storage in case we're reading a fresh system of linear equations
        self.augmented = []

        # Loop n times, reading one equation per iteration
        for i in range(self.size):
            # range(self.size) gives 0, 1, 2, ... but we usually count from 1,
            # so we display i + 1 to the user
            row = self.read_equation_row(i + 1)
            self.augmented.append(row)

    def solve_linear_system(self):
        # Choice 1: Solve a system of n linear equations in n unknowns.
        print("\n Solving a System of Linear Equations ")
        self.get_size()
        self.read_all_equations()
        self.confirm_or_edit()

        # At this point self.augmented holds the verified system.
        # Next step: actually solve it with Gaussian elimination.
        print("Matrix confirmed. Ready to solve! (We'll add this next.)")

    def find_inverse(self):
        """
        Choice 2: Find the inverse of an n x n matrix.
        Stub for now — we'll come back to this later.
        """
        print("\n--- Finding the Inverse of a Matrix ---")
        self.get_size()
        print(f"You'll be entering a {self.size}x{self.size} matrix.")