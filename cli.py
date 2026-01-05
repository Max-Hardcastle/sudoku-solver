from sudoku.solver import parse_puzzle, print_board, solve

puzzle = input("Enter Sudoku puzzle in format: 81 chars, using 0 or . for blanks:\n")
board = parse_puzzle(puzzle)

print("\nOriginal board:")
print_board(board)

if solve(board):
    print("\nSolved board:")
    print_board(board)
else:
    print("No solution exists")