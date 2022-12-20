import copy
import math
import time

from manhatten import *
from puzzleGenerator import *
import os
from puzzleGenerator import *
from hamming import *


class puzzleStateManhattan:

    """Puzzle class manhattan. each puzzle containing the manhattan distance,
    the generation (= steps into expansions), the f value (f = h + g (h = manhattan distance, g = generation)),
    and a closed boolean for already expanded puzzle states"""

    def __init__(self, puzzle, manDis, generation, f):
        self.puzzle = puzzle
        self.manDis = manDis
        self.generation = generation
        self.f = f
        self.closed = False


class puzzleStateHamming:

    """Puzzle class hamming. each puzzle containing the hamming distance,
    the generation (= steps into expansions), the f value (f = h + g (h = manhattan distance, g = generation)),
    and a closed boolean for already expanded puzzle states"""

    def __init__(self, puzzle, hamDis, generation, f):
        self.puzzle = puzzle
        self.hamDis = hamDis
        self.generation = generation
        self.f = f
        self.closed = False


class finishStats:

    """Finished stats class for returning the stats about execution to the menu for printing"""

    def __init__(self, expansions, steps, time):
        self.expansions = expansions
        self.steps = steps
        self.time = time


def printFinish(expansions, indexX):

    """debugging function for printing stats of execution"""

    drawPuzzleStart(expansions[0].puzzle)
    print("Solved")
    drawPuzzleStart(expansions[indexX].puzzle)
    print("States expanded: " + str(len(expansions)))
    print("Steps: " + str(expansions[indexX].generation))


def hamming(puzzle):

    """starting a hamming run. while loop until solution is found and stats returned to the menu"""

    start = time.time()
    startState = puzzleStateHamming(puzzle, calcHemDis(puzzle), 0, calcHemDis(puzzle))
    expansions = [startState]

    while True:
        if expand(expansions, "hamming"):
            #printFinish(expansions, len(expansions) - 1)
            break

    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), expansions[len(expansions) - 1].generation, elapsedTime)


def manhattan(puzzle):

    """starting a manhattan run. while loop until solution is found and stats returned to the menu"""

    start = time.time()
    startState = puzzleStateManhattan(puzzle, calcManDis(puzzle), 0, calcManDis(puzzle))
    expansions = [startState]

    while True:
        if expand(expansions, "manhattan"):
            #printFinish(expansions, len(expansions) - 1)
            break

    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), expansions[len(expansions) - 1].generation, elapsedTime)


def expand(expansions, algorithm):

    """expanding a state. we first search for the state with the lowest f value (f = h + g),
    where h is the hamming or manhattan distance, and g is the generation."""

    fScore = 9000
    stateIndex = 0
    for x in expansions:
        if fScore > x.f and not x.closed:
            fScore = x.f
            stateIndex = expansions.index(x)

    """following we copy the puzzle to alternate it and calculate the index, row and column
    of the blank tile to expand from there."""

    puzzle = expansions[stateIndex].puzzle
    blankIndex = puzzle.index(0)
    blankRow = math.floor(blankIndex / 3)
    blankColumn = blankIndex % 3

    """Expand down"""
    if blankRow == 0 or blankRow == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex + 3]
        puzzleDown[blankIndex + 3] = 0
        if addNewState(expansions, stateIndex, puzzleDown, algorithm):
            return True

    """Expand up"""
    if blankRow == 2 or blankRow == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 3]
        puzzleDown[blankIndex - 3] = 0
        if addNewState(expansions, stateIndex, puzzleDown, algorithm):
            return True

    """Expand left"""
    if blankColumn == 2 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 1]
        puzzleDown[blankIndex - 1] = 0
        if addNewState(expansions, stateIndex, puzzleDown, algorithm):
            return True

    """Expand right"""
    if blankColumn == 0 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex + 1]
        puzzleDown[blankIndex + 1] = 0
        if addNewState(expansions, stateIndex, puzzleDown, algorithm):
            return True

    """after expansion we set the parent tile to closed"""

    expansions[stateIndex].closed = True


def addNewState(expansions, stateIndex, puzzle, algorithm):

    """generating the new expanded state. first incrementing the generation.
    then we decide the distance and the f value and add the state to the list of expansions."""

    generation = expansions[stateIndex].generation + 1

    if algorithm == "manhattan":
        manDis = calcManDis(puzzle)
        newState = puzzleStateManhattan(puzzle, manDis, generation, manDis + generation)
        if not checkDuplicate(expansions, puzzle):
            expansions.append(newState)
            if manDis == 0:
                return True
    else:
        hamDis = calcHemDis(puzzle)
        newState = puzzleStateHamming(puzzle, hamDis, generation, hamDis + generation)
        if not checkDuplicate(expansions, puzzle):
            expansions.append(newState)
            if hamDis == 0:
                return True


def checkDuplicate(expansions, puzzle):

    """Check if a state already exists in the list of states. if so we trash it to avoid duplicates."""

    for x in expansions:
        if x.puzzle == puzzle:
            return True
    return False