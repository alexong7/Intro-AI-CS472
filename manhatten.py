import math


def calcManDis(puzzle):
    distance = 0

    """
    Calculation of the Manhattan distance. 
    Skip 0 (as 0 represents the blank tile). From an puzzle array step through the index, 
    calculating each offset (the sum of the vertical and horizontal steps needed to reach 
    its goal position) and adding it to the distance.
    
    Input: puzzle (array from 0 to 8)
    Output: Manhattan distance (int)
    """

    for i in range(9):
        if puzzle[i] == 0:
            continue

        row = math.floor(i / 3)
        column = i % 3
        actualRow = math.floor(puzzle[i] / 3)
        actualColumn = puzzle[i] % 3

        distance += abs(actualRow - row) + abs(actualColumn - column)

    return distance




