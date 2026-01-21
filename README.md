# Sudoku Solver

Command line Sudoku solver written in Python using a backtracking algorithm.

## How it works
- The user is prompted to enter a Sudoku puzzle in an 81-character Sudoku grid
- The grid state is stored, then converted to a string format which is passed to the solver
- The solver validates the initial puzzle for row, column, and 3×3 box conflicts. Invalid puzzles fail early with a clear error message, preventing long backtracking on impossible inputs
- If the board is valid but not complete, the solver finds the first empty cell and attempts each number from 1–9
- Each attempt is checked against Sudoku rules (row, column, and 3×3 box)
- Valid numbers are placed and the solver moves on to the next empty cell
- This process is performed recursively. If no valid number can be placed, the algorithm backtracks and tries a different choice
- The solver continues until the puzzle is solved or all possibilities have been exhausted
- If the puzzle is solved, the grid is populated with the completed puzzle. If it is not possible, an error is displayed.

## Usage
- Run the solver from the command line:
```bash
python app.py
```
- When prompted, enter digits into the Sudoku grid

## Testing
Pytest is used for testing

Tests cover:
- Parsing and input validation
- Rule enforcement for rows, columns and 3x3 grids
- Solver behaviour for complete valid boards, complete invalid boards, solvable boards, and unsolvable boards.

To run the tests:

```bash
pip install -r requirements.txt
python -m pytest
```

## Requirements
- Python 3.13.5
- pytest