def calcHemDis(puzzle):

    """Calculating hemming distance. this is easy af.
    we just need to check if index equals tile. if not, increment difference.

    Input: puzzle (array from 0 to 8).
    Output: hamming distance (int)"""

    distance = 0
    for i in range(0, 9):
        if puzzle[i] != i:
            distance += 1
    return distance
