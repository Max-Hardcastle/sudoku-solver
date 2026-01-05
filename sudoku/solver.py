def parse_puzzle(puzzle):
    if len(puzzle) != 81:
        raise ValueError("Error: Puzzle must be exactly 81 characters")
    
    board = []

    # Split the 81-character string into 9-character rows
    for i in range(0, 81, 9):
        row = []

        for n in puzzle[i:i+9]:
            if n in "0.":
                row.append(0)
            elif n.isdigit():
                row.append(int(n))
            else: raise ValueError("Error: Puzzle must contain digits or full stops only")
        board.append(row)

    return board


def print_board(board):
    for row in board:
        print(row)


# Check rules of the board
def is_valid(board, row, col, num):
    
    # Check row
    if num in board[row]:
        return False

    # Check columns
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check 3x3
    start_row = (row // 3) * 3 #Find row and get to first position
    start_col = (col // 3) * 3 #Find column and get to first position

    # Loop through each 3x3 and check if number already exists
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if num == board[r][c]:
                return False
    
    # True if none of the rules are broken
    return True

# Find the first empty square
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    
    return None

def solve(board):

    empty = find_empty(board)

    if empty is None:
        return True
    
    row, col = empty

    # Add valid number to each empty square, recursively call
    # and backtrack if a square has no valid input
    for n in range(1,10):
        if is_valid(board, row, col, n):
            board[row][col] = n

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False