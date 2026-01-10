# Sudoku Solver

Command line Sudoku solver written in Python using a backtracking algorithm.

## How it works
- The user is prompted to enter a Sudoku puzzle as an 81-character string (blanks are represented by `0` or `.`)
- The string is parsed into a 9×9 grid representing the Sudoku board
- If the board is full, the solver checks and confirms if the puzzle is valid
- If the board is not full, the solver finds the first empty cell and attempts each number from 1–9
- Each attempt is checked against Sudoku rules (row, column, and 3×3 box)
- Valid numbers are placed and the solver moves on to the next empty cell
- This process is performed recursively. If no valid number can be placed, the algorithm backtracks and tries a different choice
- The solver continues until the puzzle is solved or all possibilities have been exhausted

## Usage
- Run the solver from the command line:
```bash
python cli.py
```
- When prompted, enter a Sudoku string. E.g.: 530070000600195000098000060800060003400803001700020006060000280000419005000080279

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