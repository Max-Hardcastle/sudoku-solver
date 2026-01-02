board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

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


print("Original board:")
print_board(board)

if solve(board):
    print("\nSolved board:")
    print_board(board)
else:
    print("No solution exists")