# SudokuSolver
Implements a Constraint Satisfaction Problem (CSP) solver for Sudoku puzzles using Constraint Propagation and Recursive Backtracking Search. Sudoku itself is a
classic CSP where numbers are placed in a 9x9 grid such that each row, column and 3x3 box contain
all digits from 1 to 9 without repetition. <br><br>
This Program takes an incomplete Sudoku Puzzle as an input and fills in the missing numbers while adhering to the rules of Sudokue and then outputs the solution to the missing numbers. <br><br>
Sudoku text files are provided above but were downloaded from http://norvig.com/easy50.txt
# Methodology
In order to implement constraint propagation the program thinks of each cell as being a list of numbers 1-9 from which it removes numbers as they are assigned to cells in the same row, column, and box. <br><br>
For Backtracking search it is not quite as simple. We first have to think about what should happen given a puzzle. 
<ul>
<li>if it is completely filled and cell assignments are not invalid, then we have a solution;</li>
<li>if there is an invalid assignment to any cell, abort;</li>
<li>if we don’t yet have a solution and all cell assignments thus far are valid, get the next variable
and for each value in the domain of the selected variable:</li>
  <ul>
    <li>assign a value to the selected variable from the variable’s domain</li>
    <li>recursively call search to select the next variable</li>
    <li>unassign the value from the variable (the recursive call did not find a solution, so we move on to the next value in the domain)</li>
  </ul>
</ul>

# Results
The program was able to solve 50/50 puzzles.
