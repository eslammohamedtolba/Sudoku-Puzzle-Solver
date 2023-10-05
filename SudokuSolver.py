import copy

class SudokuSolver:
    # Initialize an empty list to store all sudoku solutions.
    def __init__(self):
        self.SudokuSolutions = []

    def Solver(self,SudokuPuzzle):
        # If the grid is solved, add a copy of the puzzle to the solutions list.
        if SudokuPuzzle.SolvedGrid():
            self.SudokuSolutions.append(copy.deepcopy(SudokuPuzzle))
            return
        # Iterate over each cell in the grid.
        for X in range(1,SudokuPuzzle.GridSize+1):
            for Y in range(1,SudokuPuzzle.GridSize+1):
                    # Create set of all possible values for current cell 
                    ValidValues = SudokuPuzzle.CellValidValues(X,Y)
                    for Value in ValidValues:
                        # Update Grid with new Value
                        SudokuPuzzle.Grid[X-1][Y-1]=Value
                        # Recursively solve the updated puzzle.
                        self.Solver(SudokuPuzzle)
                        # Undo the update to try other values.
                        SudokuPuzzle.Grid[X-1][Y-1]=' '
                    if ValidValues:
                        return

    # Print all solutions in the solutions list.
    def PrintSolutions(self):
        for Sudokusolution in self.SudokuSolutions:
            Sudokusolution.PrintGrid()
