# Sudoku Puzzle Solver
This is a Python package that provides classes for creating and solving Sudoku puzzles.

## SudokuPuzzle Class
The SudokuPuzzle class represents a Sudoku puzzle. It has the following methods:

### __init__(self)
This method initializes the grid size and creates an empty grid.

### CellValidValues
Return set of all possible valid values for current cell if the indices are valid and the cell is empty
the value is valid if it's not in row and column and the same sub-grid

### FillGrid(self)
This method fills the grid with values entered by the user to use it 

### PrintGrid(self)
This method prints the current state of the grid.

### SolvedGrid(self)
Check if the Grid totally filled then the grid solved by iterating over each row of the grid and check if it totally filled and doesn't contain any empty cell

## SudokuSolver Class
The SudokuSolver class represents a Sudoku solver. It has the following methods:

### __init__(self)
This method initializes an empty list to store all solutions of the provided sudoku puzzle.

### Solver(self,SudokuPuzzle)
This method takes a SudokuPuzzle object as input and recursively tries to solve it using backtracking.

PrintSolutions(self)
This method prints all solutions in the solutions list.

# Usage
To use this package, you can create an instance of the SudokuPuzzle class and call its methods to create and fill a Sudoku puzzle. 
Then, you can create an instance of the SudokuSolver class and call its methods to solve the puzzle.
