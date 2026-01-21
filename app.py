from flask import Flask, render_template, request
from sudoku.solver import parse_puzzle, solve
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    solution = None

    #9x9 grid for the UI. Strings used for inputs
    grid = [["" for _ in range(9)] for _ in range(9)]

    if request.method == "POST":
        #Build a grid based on what the user entered in the UI grid
        for r in range(9):
            for c in range(9):
                key = f"cell_{r}_{c}"
                grid[r][c] = request.form.get(key, "").strip()
        
        #Create string based on grid contents
        puzzle = ""
        for r in range(9):
            for c in range(9):
                val = grid[r][c]

                if val == "":
                    puzzle += "0"
                elif val in "123456789":
                    puzzle += val
                else:
                    error = "Error: each cell must be blank or a single digit 1-9"
                    break
            if error:
                break

        #If entry is valid, parse and solve the puzzle
        if error is None:
            try:
                board = parse_puzzle(puzzle)
                solved_board = solve(board)

                if solved_board is False:
                    error = "No solution exists for that puzzle."
                else:
                    #Display solution in the UI grid
                    for r in range(9):
                        for c in range(9):
                            grid[r][c] = str(solved_board[r][c])

            except ValueError as e:
                error = str(e)

    return render_template("index.html",
                           error=error,
                           grid=grid)

if __name__ == "__main__":
    app.run(debug=True)