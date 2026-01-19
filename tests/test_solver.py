import pytest
from sudoku.solver import parse_puzzle, solve, is_valid

#Parser function tests

def test_board_shape():
    board = parse_puzzle("." * 81) #Example valid board

    assert len(board) == 9 #Check there are 9 rows
    
    #Check each row has 9 cells
    for row in board:
        assert len(row) == 9


#Test that dots are converted to zeros
def test_dots_to_zeros():
    board = parse_puzzle("." * 81)

    assert board[0][0] == 0
    assert board[5][5] == 0


def test_invalid_char_length():
    with pytest.raises(ValueError):
        parse_puzzle("." * 82) #Input contains too many characters

def test_invalid_char_types():
    with pytest.raises(ValueError):
        parse_puzzle("x" * 81) #Input contains invalid characters

#Check that digits remain digits when parsed    
def test_digits_remain():
    board = parse_puzzle("123456789" + ("........."*8))

    assert board[0] == [1,2,3,4,5,6,7,8,9]

#Test that entries are stripped of whitespace
def test_parser_strips_whitespace():
    board = parse_puzzle("." * 81 + "\n")
    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    
#Solve function tests
def test_solve_complete_valid():
    #Complete, valid board
    board = [
    [8,2,4,9,5,3,6,7,1],
    [6,3,5,8,1,7,9,2,4],
    [7,1,9,6,2,4,8,5,3],
    [5,8,7,2,9,1,3,4,6],
    [1,4,2,7,3,6,5,8,9],
    [3,9,6,4,8,5,2,1,7],
    [2,6,1,5,4,9,7,3,8],
    [4,7,8,3,6,2,1,9,5],
    [9,5,3,1,7,8,4,6,2]
    ]

    #Check that inputting a completed, valid board returns True
    #Also check that the modified version matches original
    original = [row[:] for row in board]
    
    assert solve(board) is not False
    assert board == original

def test_solve_complete_invalid():
    #Complete, invalid board
    board = [
    [8,2,4,9,5,3,6,7,1],
    [6,3,5,8,1,7,9,2,4],
    [7,1,9,6,2,4,8,5,3],
    [8,8,7,2,9,1,3,4,6],
    [1,4,2,7,3,6,5,8,9],
    [3,9,6,4,8,5,2,1,7],
    [2,6,1,5,4,9,7,3,8],
    [4,7,8,3,6,2,1,9,5],
    [9,5,3,1,7,8,4,6,2]
    ]

    #Check that inputting an a completed but invalid board returns False
    #Also check that the modified version matches original
    original = [row[:] for row in board]
    
    assert solve(board) is False
    assert board == original

def test_solvable():
    board = [
    [8,0,0,0,0,5,0,0,0],
    [0,7,0,9,0,0,0,4,0],
    [0,0,9,0,7,8,3,2,5],
    [3,0,1,0,9,0,0,5,0],
    [0,0,6,0,0,0,1,0,0],
    [0,9,0,0,3,0,6,0,2],
    [2,8,3,6,5,0,7,0,0],
    [0,1,0,0,0,2,0,8,0],
    [0,0,0,1,0,0,0,0,9]
    ]

    #Check that an incomplete, solvable board returns True
    assert solve(board) is not False
    #Check no zeros remain
    assert all(cell != 0 for row in board for cell in row)

def test_unsolvable():
    board = [
    [1,2,3,4,5,6,7,8,9],
    [0,0,0,0,0,0,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    #Check that an incomplete, unsolvable board returns False
    assert solve(board) is False

#is_valid function tests

#Duplicate in row
def test_row_dup_validity():    
    board = [
    [0,0,0,0,0,0,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    assert is_valid(board, 0, 8, 8) is False

#Duplicate in column
def test_col_dup_validity():    
    board = [
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    assert is_valid(board, 1, 0, 1) is False

#Duplicate in 3x3
def test_grid_dup_validity():    
    board = [
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    assert is_valid(board, 1, 1, 1) is False

#Test a valid input is accepted
def test_valid_entry():
    board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    assert is_valid(board, 0, 0, 1)