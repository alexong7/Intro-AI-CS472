import math


def calcManDis(puzzle):
    difference = 0

    """Calculate the manhattan distance. skip 0 (as 0 represents the blank tile).
    from an puzzle array we step through the index, calculating each offset and adding
    it to the difference.
    
    Input: puzzle (array from 0 to 8).
    Output: manhattan distance (int)"""

    for i in range(9):
        if puzzle[i] == 0:
            continue

        row = math.floor(i / 3)
        column = i % 3
        actualRow = math.floor(puzzle[i] / 3)
        actualColumn = puzzle[i] % 3

        difference += abs(actualRow - row) + abs(actualColumn - column)

    return difference




