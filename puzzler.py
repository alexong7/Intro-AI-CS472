import copy
import time

from manhatten import *
from hamming import *


class puzzleStateManhattan:

    """
    Puzzle class manhattan. Each puzzle containing
    - h = manhattan distance (calculated in manhattan.py)
    - g = generation (path cost from the initial state to node)
    - f = f value, f = g + h (estimated cost of the best path that continues from node to goal state)
    - and a closed boolean for already expanded puzzle states.
    """

    def __init__(self, puzzle, manDis, generation, f):
        self.puzzle = puzzle
        self.manDis = manDis
        self.generation = generation
        self.f = f
        self.closed = False


class puzzleStateHamming:

    """
    Puzzle class hamming. Each puzzle containing
    - h = hamming distance (calculated in hamming.py)
    - g = generation (path cost from the initial state to node)
    - f = f value, f = g + h (estimated cost of the best path that continues from node to goal state)
    - and a closed boolean for already expanded puzzle states.
    """

    def __init__(self, puzzle, hamDis, generation, f):
        self.puzzle = puzzle
        self.hamDis = hamDis
        self.generation = generation
        self.f = f


class finishStats:

    """
    FinishStats class for returning the stats about puzzle execution to menu.py for printing.
    """

    def __init__(self, expansions, steps, time):
        self.expansions = expansions
        self.steps = steps
        self.time = time


def hamming(puzzle):

    """
    Starting a hamming run. while loop, until solution is found and stats are returned to menu.py.

    Input: starting node
    Output: stats about execution (time, steps, expanded nodes)
    """

    start = time.time()
    startState = puzzleStateHamming(puzzle, calcHamDis(puzzle), 0, calcHamDis(puzzle))
    expansions = [startState]
    open = [startState]

    while True:
        if expand(expansions, open, "hamming"):
            break

    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), expansions[len(expansions) - 1].generation, elapsedTime)


def manhattan(puzzle):

    """
    Starting a manhattan run. while loop, until solution is found and stats returned to menu.py.

    Input: starting node
    Output: stats about execution (time, steps, expanded nodes)
    """

    start = time.time()
    startState = puzzleStateManhattan(puzzle, calcManDis(puzzle), 0, calcManDis(puzzle))
    expansions = [startState]
    open = [startState]

    while True:
        if expand(expansions, open, "manhattan"):
            break

    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), expansions[len(expansions) - 1].generation, elapsedTime)


def expand(expansions, open, algorithm):

    """
    Expansion of a state. First search for the state with the lowest f value (f = h + g),
    where h is the hamming or manhattan distance, and g is the generation.

    Input: list of all nodes, algorithm
    Output: true if solution
    """

    fScore = 9000
    stateIndex = 0
    for x in open:
        if fScore > x.f:
            fScore = x.f
            stateIndex = open.index(x)

    """
    Next, copy the puzzle to alternate it and calculate the index, row and column
    of the blank tile to expand from there.
    """

    puzzle = open[stateIndex].puzzle
    blankIndex = puzzle.index(0)
    blankRow = math.floor(blankIndex / 3)
    blankColumn = blankIndex % 3
    generation = open[stateIndex].generation

    """
    Expand down
    """
    if blankRow == 0 or blankRow == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex + 3]
        puzzleDown[blankIndex + 3] = 0
        if addNewState(expansions, open, generation, puzzleDown, algorithm):
            return True

    """
    Expand up
    """
    if blankRow == 2 or blankRow == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 3]
        puzzleDown[blankIndex - 3] = 0
        if addNewState(expansions, open, generation, puzzleDown, algorithm):
            return True

    """
    Expand left
    """
    if blankColumn == 2 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 1]
        puzzleDown[blankIndex - 1] = 0
        if addNewState(expansions, open, generation, puzzleDown, algorithm):
            return True

    """
    Expand right
    """
    if blankColumn == 0 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex + 1]
        puzzleDown[blankIndex + 1] = 0
        if addNewState(expansions, open, generation, puzzleDown, algorithm):
            return True

    """
    After expansion parent generation is set to closed.
    """

    open.remove(open[stateIndex])

    for x in open:
        if x.generation == generation - 1:
            open.remove(x)

def addNewState(expansions, open, generation, puzzle, algorithm):

    """
    Generation of the new expanded state. First incrementing the generation,
    then calculating hamming or manhattan distance and the f value,
    and adding the state to the list of expansions.

    Input: list of all nodes, index of parent node, new node, algorithm
    Output: true if solution
    """

    if algorithm == "manhattan":
        manDis = calcManDis(puzzle)
        newState = puzzleStateManhattan(puzzle, manDis, generation + 1, manDis + generation)
        if not checkDuplicate(expansions, puzzle):
            expansions.append(newState)
            open.append(newState)
            if manDis == 0:
                return True
    else:
        hamDis = calcHamDis(puzzle)
        newState = puzzleStateHamming(puzzle, hamDis, generation + 1, hamDis + generation)
        if not checkDuplicate(expansions, puzzle):
            expansions.append(newState)
            open.append(newState)
            if hamDis == 0:
                return True


def checkDuplicate(expansions, puzzle):

    """
    Check if a state already exists in the list of states. If so, it is trashed to avoid duplicates.

    Input: list of all expanded nodes, new node
    Output: true or false
    """

    for x in expansions:
        if x.puzzle == puzzle:
            return True
    return False
