class GaussSolver:

    # Solves a system of n linear equations in n unknowns using
    # Gauss-Jordan elimination with partial pivoting.

    def __init__(self, augmented, n):

        # Parameters:
        # augmented: the augmented matrix [A | b] as a list of lists.
        # Each row has n + 1 entries: n coefficients + 1 constant.
        # n: the number of equations and unknowns.

        self.augmented = augmented
        self.n = n

        # The full row width is n coefficients + 1 constant column
        self.total_cols = n + 1

        # Will be set to True if the system has no unique solution
        self.is_singular = False

        # Will hold the final solution [x1, x2, ..., xn] once we compute it
        self.solution = None

    def solve(self):
        """
        Run Gauss-Jordan elimination on self.augmented to find the solution.
        After this method runs:
        - If the system has a unique solution, self.solution holds the values.
        - If the matrix is singular, self.is_singular becomes True
          and self.solution stays as None.
        """
        # We'll fill this in step by step
        pass