def calcHamDis(puzzle):

    """
    Calculation of Hamming distance
    Check if puzzle array index equals tile, i.e. tile is in the right place.
    If not, increment distance.

    Input: puzzle (array from 0 to 8)
    Output: Hamming distance (int)
    """

    distance = 0
    for i in range(0, 9):
        if puzzle[i] != i:
            distance += 1
    return distance
