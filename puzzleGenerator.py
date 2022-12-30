import random

allVariations = []


def fixedPuzzles():

    """
    For testing
    """

    return [[7, 1, 0, 8, 6, 2, 5, 4, 3], [7, 2, 8, 0, 4, 3, 5, 1, 6], [7, 2, 0, 6, 3, 4, 5, 1, 8], [8, 0, 5, 4, 2, 7, 6, 1, 3], [7, 2, 6, 3, 1, 5, 8, 4, 0], [0, 7, 4, 5, 8, 2, 1, 6, 3], [5, 4, 8, 7, 1, 2, 0, 3, 6], [5, 7, 0, 8, 3, 1, 4, 6, 2], [1, 4, 6, 5, 8, 2, 3, 7, 0], [6, 7, 0, 1, 4, 3, 5, 2, 8], [3, 0, 5, 2, 4, 1, 7, 6, 8], [1, 5, 8, 3, 6, 7, 4, 0, 2], [6, 7, 4, 3, 1, 2, 8, 5, 0], [4, 3, 8, 2, 0, 1, 5, 7, 6], [3, 5, 8, 6, 4, 0, 1, 7, 2], [4, 3, 0, 8, 1, 7, 6, 5, 2], [7, 1, 5, 6, 4, 3, 0, 8, 2], [4, 5, 3, 7, 2, 0, 8, 1, 6], [3, 6, 2, 4, 8, 0, 5, 1, 7], [5, 0, 1, 4, 8, 7, 6, 3, 2], [5, 4, 7, 0, 1, 2, 6, 3, 8], [4, 8, 7, 5, 0, 2, 1, 3, 6], [7, 6, 0, 4, 5, 8, 1, 2, 3], [2, 6, 7, 0, 4, 1, 5, 3, 8], [0, 6, 1, 7, 8, 4, 5, 3, 2], [1, 5, 2, 7, 0, 6, 8, 3, 4], [0, 1, 3, 8, 4, 7, 5, 6, 2], [7, 0, 6, 3, 4, 2, 8, 1, 5], [4, 5, 6, 8, 1, 0, 3, 2, 7], [4, 2, 8, 6, 0, 3, 1, 7, 5], [2, 4, 6, 0, 1, 5, 7, 3, 8], [7, 3, 4, 8, 6, 0, 5, 2, 1], [0, 6, 8, 4, 3, 7, 2, 1, 5], [5, 4, 0, 8, 3, 7, 2, 1, 6], [8, 1, 3, 0, 5, 7, 4, 2, 6], [4, 2, 6, 7, 1, 3, 5, 8, 0], [6, 8, 4, 5, 0, 7, 3, 1, 2], [6, 5, 7, 0, 1, 3, 8, 2, 4], [2, 4, 5, 0, 6, 3, 8, 1, 7], [5, 3, 6, 1, 4, 8, 2, 7, 0], [0, 3, 8, 4, 5, 1, 6, 7, 2], [7, 4, 8, 0, 5, 1, 3, 2, 6], [8, 4, 7, 5, 2, 3, 1, 6, 0], [3, 5, 6, 8, 7, 0, 4, 2, 1], [6, 5, 3, 0, 4, 1, 7, 2, 8], [2, 0, 3, 5, 1, 7, 4, 6, 8], [0, 3, 6, 5, 8, 7, 4, 1, 2], [3, 2, 4, 0, 1, 7, 8, 5, 6], [0, 5, 8, 6, 4, 7, 1, 2, 3], [8, 7, 3, 4, 0, 1, 6, 5, 2], [7, 1, 8, 3, 6, 4, 2, 0, 5], [5, 4, 1, 8, 0, 7, 3, 6, 2], [8, 4, 2, 1, 7, 5, 6, 3, 0], [7, 3, 1, 6, 2, 5, 0, 4, 8], [8, 0, 3, 1, 4, 6, 5, 7, 2], [7, 0, 6, 4, 2, 3, 8, 1, 5], [7, 1, 0, 2, 3, 6, 8, 4, 5], [2, 8, 5, 7, 6, 4, 3, 0, 1], [3, 6, 5, 7, 4, 2, 0, 8, 1], [7, 0, 3, 5, 1, 8, 6, 2, 4], [6, 0, 8, 2, 5, 7, 4, 1, 3], [0, 5, 3, 6, 2, 4, 7, 1, 8], [1, 4, 3, 8, 7, 2, 5, 6, 0], [6, 3, 2, 4, 8, 1, 0, 5, 7], [8, 1, 5, 0, 4, 7, 6, 3, 2], [1, 3, 0, 6, 8, 7, 2, 5, 4], [4, 6, 0, 1, 5, 7, 2, 8, 3], [4, 7, 1, 6, 0, 5, 8, 3, 2], [3, 2, 8, 5, 4, 1, 7, 6, 0], [1, 0, 6, 3, 5, 7, 4, 2, 8], [8, 6, 0, 4, 5, 3, 1, 2, 7], [6, 0, 2, 7, 3, 8, 5, 1, 4], [2, 4, 8, 6, 7, 1, 3, 0, 5], [1, 0, 2, 6, 8, 4, 3, 5, 7], [8, 4, 1, 6, 5, 0, 2, 7, 3], [7, 6, 4, 1, 8, 3, 2, 0, 5], [1, 0, 8, 5, 3, 7, 4, 2, 6], [5, 2, 3, 4, 8, 6, 7, 1, 0], [1, 2, 4, 5, 0, 8, 6, 3, 7], [3, 8, 2, 7, 1, 0, 5, 4, 6], [4, 2, 6, 3, 8, 1, 7, 5, 0], [6, 3, 4, 0, 1, 7, 2, 8, 5], [3, 7, 1, 0, 2, 8, 4, 5, 6], [3, 1, 6, 0, 4, 2, 7, 8, 5], [0, 4, 6, 1, 3, 8, 2, 7, 5], [2, 0, 5, 3, 6, 1, 8, 7, 4], [1, 2, 0, 4, 7, 3, 6, 8, 5], [3, 6, 5, 4, 1, 2, 8, 7, 0], [8, 3, 1, 0, 4, 6, 5, 7, 2], [2, 5, 6, 7, 3, 1, 0, 8, 4], [5, 8, 3, 0, 4, 6, 1, 2, 7], [0, 6, 4, 8, 3, 1, 2, 7, 5], [1, 4, 6, 8, 3, 0, 5, 7, 2], [3, 5, 6, 2, 0, 8, 4, 7, 1], [2, 4, 7, 6, 0, 3, 5, 1, 8], [2, 4, 1, 0, 3, 7, 5, 8, 6], [0, 6, 7, 8, 4, 3, 5, 1, 2], [7, 1, 8, 0, 4, 6, 3, 5, 2], [6, 1, 3, 2, 0, 5, 7, 4, 8], [2, 7, 8, 4, 6, 3, 5, 0, 1]]

def createPuzzle():

    """
    From a predefined array with all possible values (tiles 1 to 8, 0 represents the blank tile)
    a random value is picked and added to a new array which is the start state for the puzzle.

    Output: a puzzle (array from 0 to 8)
    """

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    numbersArrangement = []
    for i in range(9):
        tempNumber = random.choice(numbers)
        numbers.remove(tempNumber)
        numbersArrangement.append(tempNumber)
    return numbersArrangement


def drawPuzzleStart(puzzle):

    """
    The puzzle is drawn in a 3x3 grid.

    Input: puzzle (array from 0 to 8)
    Output: in console
    """

    for i in range(0, 9):
        print(" ", end="")
        print(puzzle[i], end="")
        if (i + 1) % 3 != 0:
            print(" |", end="")
        else:
            print("\n", end="")


def checkSolvability(checkPuzzle):

    """
    Checking for the count of number pairs, where the higher number appears before the lower number.
    If those pairs appear an odd amount of times the puzzle is not solvable.

    Input: puzzle (array from 0 to 8)
    Output: true or false
    """

    evenOrOdd = 0
    for i in range(0, 9):
        for j in range(i+1, 9):
            if checkPuzzle[i] != 0 and checkPuzzle[j] != 0 and checkPuzzle[i] > checkPuzzle[j]:
                evenOrOdd+=1

    return evenOrOdd % 2 == 0


def create100Variations():
    while len(allVariations) < 100:

        """
        Generation of all 100 variations using the createPuzzle() methode. Each variation 
        is checked for solvability, and if solvable it is added to the list of valid variations.
        
        Output: list of puzzles
        """
        tempArray = createPuzzle()

        if checkSolvability(tempArray):
            allVariations.append(tempArray)

    return allVariations
