def parse_puzzle(puzzle):
    puzzle = puzzle.strip()
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

    check_initial_puzzle(board)
    return board
    

#Function to check the entered puzzle is valid, to prevent long backtracking for impossible puzzles
def check_initial_puzzle(board):

    #Check each row for duplicates
    for row in range(0, 9):
        nums = [n for n in board[row] if n != 0]
        if len(nums) != len(set(nums)):
            raise ValueError(f"Error: Invalid starting board, duplicate in row {row+1}")

    #Check each column for duplicates  
    for col in range(0, 9):
        col_vals = [board[row][col] for row in range(9)]
        col_vals = [n for n in col_vals if n != 0]

        if len(col_vals) != len(set(col_vals)):
            raise ValueError(f"Error: Invalid starting board, duplicate in column {col+1}")

    # Loop through each 3x3 check for duplicates
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            grid_tocheck = []
            for r in range(0,3):
                for c in range(0,3):
                    grid_tocheck.append(board[row_start + r][col_start + c])
            
            grid_vals = [n for n in grid_tocheck if n != 0]
            
            if len(grid_vals) != len(set(grid_vals)):
                raise ValueError(f"Error: Invalid starting board, duplicate in grid starting column: {col_start+1} row: {row_start+1}")
            
    return True


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

#Function to check that completed boards that are inputted are valid
def is_board_valid(board):

    valid = [1,2,3,4,5,6,7,8,9]

    # Sort each row and check it contains 1-9
    for row in range(0, 9):
        if sorted(board[row]) != valid:
            return False

    # Sort each column and check it contains 1-9    
    for col in range(0, 9):
        col_vals = [board[row][col] for row in range(9)]
        if sorted(col_vals) != valid:
            return False
        
    # Loop through each 3x3 check it contains 1-9
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            grid_tocheck = []
            for r in range(0,3):
                for c in range(0,3):
                    grid_tocheck.append(board[row_start + r][col_start + c])
            if sorted(grid_tocheck) != valid:
                return False
    
    return True
        
    
def solve(board):
    empty = find_empty(board)

    #Check that completed boards are valid
    if empty is None:
        if is_board_valid(board):
            return board
        else: return False
    
    row, col = empty

    # Add valid number to each empty square, recursively call
    # and backtrack if a square has no valid input
    for n in range(1,10):
        if is_valid(board, row, col, n):
            board[row][col] = n

            result = solve(board)
            if result is not False:
                return result
            
            board[row][col] = 0
    
    return False