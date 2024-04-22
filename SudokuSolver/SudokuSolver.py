# Name: Jared Schneider 
# Program Description: Implement a Constraint Satisfaction Problem (CSP) solver for Sudoku puzzles.
# Note: Change 'filename' at top of file to use different puzzles. Puzzles were found at http://norvig.com/easy50.txt
# Compile: "python SudokuSolver.py"
#
# Documentation used:
# Re - https://docs.python.org/3/library/re.html

import re

filename = 'sudoku_puzzles.txt'

def cross(A, B):
    return [a + b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], [])) - {s}) for s in squares)

def grid_values(grid):
    return dict(zip(squares, grid))

def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values

#Constraint Propagation function
def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

#Constraint Propagation helper function: Eliminate Possible Values
def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def solve(grid):
    return search(parse_grid(grid))

#Recursive backtracking function 
def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    for e in seq:
        if e: return e
    return False

def print_grid(values):
    for r in rows:
        #Inverse the commented lines for nice readability output
        print(''.join(values[r + c] for c in cols))
        #temp = ''.join(values[r + c] for c in cols)
        #print(litering_by_three(temp))
        #if r in 'CF': print('')

#Helper function to split up every 3 characters
def litering_by_three(a):
    return " ".join([a[::-1][i:i+3] for i in range(0, len(a), 3)])[::-1]

def solve_and_print(grid):
    solution = solve(grid)
    if solution:
        print_grid(solution)
        print('===========')
        return True
    else:
        print("No solution exists.")
        print('===========')
        return False
    
# Read and solve each puzzle from the input file
puzzle_count = 0
solved_count = 0
with open(filename, 'r') as file:
    puzzle = ''
    for line in file:
        line = line.strip()
        if line == '========':
            if solve_and_print(puzzle):
                solved_count += 1
            puzzle_count += 1
            puzzle = ''
        else:
            puzzle += re.sub(r'\D', '0', line)

# Solve the last puzzle in the file
if puzzle and solve_and_print(puzzle):
    solved_count += 1
    puzzle_count += 1

print(f"Solved {solved_count} out of {puzzle_count} puzzles.")
