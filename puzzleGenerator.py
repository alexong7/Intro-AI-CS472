import random

allVariations = []

def createPuzzle():

    """
    From an predefined array with all possible values we pick a random value and add it
    to a new array which is our start state for the puzzle.
    """

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, "."]
    numbersArrangement = []
    for i in range(9):
        tempNumber = random.choice(numbers)
        numbers.remove(tempNumber)
        numbersArrangement.append(tempNumber)
    return numbersArrangement
    #drawPuzzleStart(numbersArrangement)


def drawPuzzleStart(puzzleArray):

    """ we draw the puzzle in a 3x3 grid """

    for i in range(0, 9):
        print(" ", end="")
        print(puzzleArray[i], end="")
        if (i + 1) % 3 != 0:
            print(" |", end="")
        else:
            print("\n", end="")


def checkSolvability(checkArray):

    """
    Here we check for the amount of number pairs, where the higher number appears before the lower number.
    If those pairs appear an even amount of times the puzzle is not solvable.
    We return true or false.
    """

    evenOrOdd = 0
    for i in range(0, 9):
        for j in range(i+1, 9):
            if checkArray[i] != "." and checkArray[j] != "." and checkArray[i] > checkArray[j]:
                evenOrOdd+=1

    #print(evenOrOdd)
    return evenOrOdd % 2 == 0


def create100Variations():
    while len(allVariations) < 99:

        """
        Here we generate all the 100 variations with the createPuzzle() methode. We check each
        variation for solvability and if solvable we add it to our list of valid variations.
        """
        tempArray = createPuzzle()

        if checkSolvability(tempArray):
            allVariations.append(tempArray)

    return allVariations
    #print(allVariations)