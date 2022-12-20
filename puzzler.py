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

    def __init__(self, expansions, steps, time):
        self.expansions = expansions
        self.steps = steps
        self.time = time


def printFinish(expansions, indexX):
    drawPuzzleStart(expansions[0].puzzle)
    print("Solved")
    drawPuzzleStart(expansions[indexX].puzzle)
    print("States expanded: " + str(len(expansions)))
    print("Steps: " + str(expansions[indexX].generation))


def hamming(puzzle):
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
    fScore = 9000
    stateIndex = 0
    for x in expansions:
        if fScore > x.f and not x.closed:
            fScore = x.f
            stateIndex = expansions.index(x)

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

    expansions[stateIndex].closed = True


def addNewState(expansions, stateIndex, puzzle, algorithm):
    generation = expansions[stateIndex].generation + 1

    if algorithm == "manhattan":
        manDis = calcManDis(puzzle)
        newState = puzzleStateManhattan(puzzle, manDis, generation, manDis + generation)
        if not checkDublicate(expansions, puzzle):
            expansions.append(newState)
            if manDis == 0:
                return True
    else:
        hamDis = calcHemDis(puzzle)
        newState = puzzleStateHamming(puzzle, hamDis, generation, hamDis + generation)
        if not checkDublicate(expansions, puzzle):
            expansions.append(newState)
            if hamDis == 0:
                return True


def checkDublicate(expansions, puzzle):
    for x in expansions:
        if x.puzzle == puzzle:
            return True
    return False