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

    def forward_elimination(self):

        # Phase 1: Reduce the matrix to row-echelon form
        # Makes all entries below the diagonal zero.

        for k in range(self.n):

            #Partial pivoting
            # Find the row at or below k with the largest absolute value in column k
            max_row = k
            max_val = abs(self.augmented[k][k])
            for r in range(k + 1, self.n):
                if abs(self.augmented[r][k]) > max_val:
                    max_val = abs(self.augmented[r][k])
                    max_row = r

            # Swap that row up to position k
            if max_row != k:
                self.augmented[k], self.augmented[max_row] = (
                    self.augmented[max_row], self.augmented[k]
                )

            #  Singular check to see if the equation has a solution
            if abs(self.augmented[k][k]) < 1e-12:
                self.is_singular = True
                return

            # Eliminate below the pivot
            # range starts at k + 1, so we only touch rows BELOW k.
            # Rows above k stay exactly as they are.
            for r in range(k + 1, self.n):
                # The factor that, when multiplied with the pivot row,
                # gives us exactly what's at [r][k] — so subtracting
                # zeros out that entry.
                factor = self.augmented[r][k] / self.augmented[k][k]

                # Subtract factor × pivot row from row r, across all columns
                for c in range(self.total_cols):
                    self.augmented[r][c] = (
                            self.augmented[r][c] - factor * self.augmented[k][c]
                    )

    def solve(self):

        # Runs Gaussian elimination + back-substitution to find the solution.

        # Phase 1: Reduce the equation to row-echelon form
        self.forward_elimination()

        # If the matrix is singular, no unique solution exists — stop here
        if self.is_singular:
            return

        # Phase 2: Back-substitute to get the unknowns
        self.back_substitution()