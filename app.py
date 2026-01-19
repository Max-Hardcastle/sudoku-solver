from flask import Flask, render_template, request
from sudoku.solver import parse_puzzle, solve
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    solution = None
    puzzle = ""

    #On POST request, populate puzzle with what is entered in textarea
    if request.method == "POST":
        error = None
        solution = None
        puzzle = request.form["puzzle"]

    #Parse entered puzzle, attempt to solve, pass solution/no solution/error to html
        try:
            board = parse_puzzle(puzzle)
            solved = solve(board)

            if solved != False:
                solution = solved
            else:
                error = "No solution exists for the entered puzzle"
        except ValueError as e:
            error = str(e)

    return render_template("index.html", error=error, solution=solution, puzzle=puzzle)


if __name__ == "__main__":
    app.run(debug=True)