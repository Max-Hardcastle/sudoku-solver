def parse_puzzle(puzzle):
    if len(puzzle) != 81:
        raise ValueError("Error: Puzzle must be exactly 81 characters")
    
    board = []

    for i in range (0, 81, 9):
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


#Check rules of the board
def check_entry(board, row, col, num):
    
#Check row
    if num in board[row]:
        return False

#Check columns
    for r in range(9):
        if board[r][col] == num:
            return False

#Check 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if num == board[r][c]:
                return False
    
    #True if none of the rules are broken
    return True


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    
    return None

def solve(board):

    empty = find_empty(board)

    if empty == None:
        return True
    
    row, col = empty

    for n in range(1,10):
        if check_entry(board, row, col, n):
            board[row][col] = n

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False


if __name__ == "__main__":
    puzzle = input("Enter Sudoku puzzle in format: 82 chars, using 0 or . for blanks:\n")
    board = parse_puzzle(puzzle)

    print("\nOriginal board:")
    print_board(board)

    if solve(board):
        print("\nSolved board:")
        print_board(board)
    else:
        print("No solution exists")