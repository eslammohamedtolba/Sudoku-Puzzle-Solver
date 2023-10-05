from math import sqrt

class SudokuPuzzle:
    # Initialize the grid size and create an empty grid.
    def __init__(self):
        while True:
            self.GridSize = int(input("Enter Grid Size that is squared number: "))
            if self.GridSize>0 and sqrt(self.GridSize)*sqrt(self.GridSize)==self.GridSize:
                break
        self.Grid = [[' ']*self.GridSize for _ in range(self.GridSize)]
        self.squareSize = int(sqrt(self.GridSize))
        
    # Return set of all possible valid values for current cell if the indices are valid and the cell is empty
    # the value is valid value if it is not in row and column and the same sub-grid
    def CellValidValues(self,X,Y):
        if (X in range(1,self.GridSize+1)) and (Y in range(1,self.GridSize+1)) and self.Grid[X-1][Y-1]==' ':
            # find all values of subgrid for current cell
            startX = ((X-1)//self.squareSize)*self.squareSize
            startY = ((Y-1)//self.squareSize)*self.squareSize
            Listsquare = []
            for x in range(startX,startX+self.squareSize):
                for y in range(startY,startY+self.squareSize):
                    if self.Grid[x][y]!=' ':
                        Listsquare.append(self.Grid[x][y])
            return (set(range(1,self.GridSize+1)) - set(self.Grid[X-1]+[row[Y-1] for row in self.Grid]+Listsquare))
        return {}
    
    # Fill the grid with values entered by the user to create his puzzle filled by some values
    def FillGrid(self):
        SizeFilling = 0
        while True:
            SizeFilling = int(input("Enter Filling size: "))
            if SizeFilling in range(self.GridSize*self.GridSize):
                break
        for IndexEnter in range(SizeFilling):
            while True:
                X = int(input(f"Enter X-axis of input number {IndexEnter+1}: "))
                Y = int(input(f"Enter Y-axis of input number {IndexEnter+1}: "))
                Value = int(input(f"Enter the Value from 1 to {self.GridSize}: "))
                
                # Check if the Value user entered in cell valid values
                if Value in self.CellValidValues(X,Y):
                    self.Grid[X-1][Y-1] = Value
                    self.PrintGrid()
                    break

    # Print the current state of the grid.
    def PrintGrid(self):
        print()
        print("--------"*self.GridSize+"-"*(1+self.GridSize))
        for i in range(self.GridSize):
            print("| ",end="")
            for j in range(self.GridSize):
                print(f"   {self.Grid[i][j]}  " if self.Grid[i][j]!=' ' else f"{i+1,j+1}",end = ' | ')
            print()
            print("--------"*self.GridSize+"-"*(1+self.GridSize))
        print()
    
    # Check if the Grid totally filled then the grid solved 
    # by iterating over each row of the grid and check if it totally filled and doesn't contain any empty cell
    def SolvedGrid(self):
        for row in self.Grid:
            if row.count(' ')>0:
                return False
        return True