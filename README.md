# Gaussian Elimination Calculator

## Overview

The Gaussian Elimination Calculator is a Python console application that solves
systems of linear equations using the Gaussian Elimination method with transforming the matrix to row echelon form and back-substitution. 
The program accepts equations in natural form
(e.g., `3x + 5y - 6z = 8`), parses them automatically, lets the user verify or
edit the resulting matrix, and then computes the values of the unknowns. It can only handle 3 or 4 unknowns in the system of linear equations.
It is built using Object-Oriented Programming (OOP) principles, with each
responsibility (menu, input handling, math computation) cleanly separated into
its own class and file. 
## Files

**main.py** — The entry point of the program. Displays the main menu and
dispatches the user's choice to the appropriate operation.

**systems_manager.py** — Contains the `SystemsManager` class, the "brain" of
the program. It collects the user's equations, validates input, builds the
augmented matrix, and displays the final solution.

**gauss_solver.py** — Contains the `GaussSolver` class, which performs the
actual mathematical work: forward elimination after transforming the matrix to row-echelon form, followed
by back-substitution.

## Features

- Accepts equations written in natural form (e.g., `3x + 5y - 6z = 8`).
- Supports systems of size 3×3 (variables x, y, z) or 4×4 (x, y, z, w) only.
- Parses equations regardless of variable order or spacing.
- Displays the augmented matrix [A | b] for user verification before solving.
- Allows the user to edit any individual row if they spot an error in the matrix displayed.
- Detects singular matrices and reports when no unique solution exists.
- Uses partial pivoting for numerical stability.
- Displays the final solution with proper variable names (x, y, z, w).

## How It Works

The program implements **Gaussian Elimination with back-substitution**, a
classical method for solving systems of linear equations:

1. **Build the augmented matrix [A | b]** from the user's equations.
2. **Forward elimination**: use elementary row operations to reduce the matrix
   to row echelon form (zeros below the diagonal). At each pivot column,
   the row with the largest absolute value in that column is swapped up to
   improve numerical accuracy — this is called *partial pivoting*.
3. **Back-substitution**: starting from the last row (which now contains a
   single unknown), solve for each variable, plugging known values back into
   earlier rows to find the remaining unknowns one at a time.

If at any point the algorithm cannot find a non-zero pivot, the matrix is
declared singular and the program reports that no unique solution exists.

## Requirements

- Python 3.7 or higher
- No external libraries — uses only the Python standard library

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the program: python main.py
4. Follow the on-screen prompts to choose an operation, enter the size of the
   system, and type each equation.
   
## Example Usage
Hello, which System of Linear Equations are you looking to solve today?

Enter the number of variables in your equations (3 or 4):3

--- Input Mode: Enter equations using x, y, z ---

Example: 3x + 5y - 6z = 8

Equation 1: 2x + y - z = 8
Equation 2: -3x - y + 2z = -11
Equation 3: -2x + y + 2z = -3

Here's the augmented matrix [A | b] we built from your equations:

Row 1:  [      2       1      -1  |       8 ]
Row 2:  [     -3      -1       2  |     -11 ]
Row 3:  [     -2       1       2  |      -3 ]

Is this correct? (yes to continue, no to edit a row): yes

Solution:
x = 2
y = 3
z = -1

## Author
Patmos Acher Mpakaniye
