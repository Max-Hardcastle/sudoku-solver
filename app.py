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
        for r in range(9):
            for c in range(9):
                key = f"cell_{r}_{c}"
                grid[r][c] = request.form.get(key, "").strip()

    return render_template("index.html",
                           error=error,
                           solution=solution,
                           grid=grid)


if __name__ == "__main__":
    app.run(debug=True)