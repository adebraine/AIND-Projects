import os.path
from My_utils import *
import new_sudoku
import sys

""" [Level of Difficulty] = Input the level of difficulty of the sudoku puzzle. Difficulty levels
    include ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
    difficulty."""
level = "Easy"
new_sudoku.main(level)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [[rows[i]+cols[i] for i in range(len(rows))],[rows[i]+cols[len(rows)-1-i] for i in range(len(rows))]]

""" Sudoku type = diagonal sudoku or regular sudoku. """
sudoku_type = 'regular'

if sudoku_type == 'diagonal':
    unitlist = row_units + column_units + square_units + diagonal_units
elif sudoku_type == 'regular':
    unitlist = row_units + column_units + square_units
else:
    print('Wrong Sudoku type or Unsupported Sudoku type')
    print('sudoku_type = diagonal or regular')
    sys.exit()

# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)

def naked_twins(values):
    all_twin_values = [box for box in values.keys() if len(values[box]) == 2]
    twin_values = []
    for box1 in all_twin_values:
        for box2 in peers[box1]:
            if values[box1] == values[box2]:
                twin_values.append([box1,box2])
    for i in range(len(twin_values)):
        box = twin_values[i]
        peers_twin = set(peers[box[0]]).intersection(set(peers[box[1]]))
        for peer in peers_twin:
            if len(values[peer]) > 1:
                for rv in values[box[0]]:
                    values = assign_value(values,peer,values[peer].replace(rv,''))
#                    values[peer] = values[peer].replace(rv,'')
    return values

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values,peer,values[peer].replace(digit,''))
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values,dplaces[0],digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    values = grid2values(grid)
    values = search(values)
    return values

if __name__ == "__main__": 
    if os.path.isfile("Sudoku.txt"):
        Fc = open("Sudoku.txt", "r")
        diag_sudoku_grid = Fc.read()
        Fc.close()
    elif not os.path.isfile("Sudoku.txt"):
        diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    
    if sudoku_type == 'diagonal':
        diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    
    
#    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)
    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
