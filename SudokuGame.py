'''
Sudoku is a popular number puzzle game that is based on logic, the game consists of a nxn grid of small squares and n must be square number
The Game objective is to fill the grid with numbers so that each column, row, and sub-grid contains all the numbers between 1 and n without any repeats.
'''
from SudokuPuzzle import *
from SudokuSolver import *

# Create sudoku puzzle
sdkpuzzle = SudokuPuzzle()
sdkpuzzle.PrintGrid()
sdkpuzzle.FillGrid()

# Solve sudoku puzzle
sdksolver = SudokuSolver()
sdksolver.Solver(sdkpuzzle)
sdksolver.PrintSolutions()

