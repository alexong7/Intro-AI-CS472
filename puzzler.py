import copy
import math
from manhatten import *
from puzzleGenerator import *
import os


goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class puzzleState:

    def __init__(self, puzzle, manDis, generation, f):
        self.puzzle = puzzle
        self.manDis = manDis
        self.generation = generation
        self.f = f
        self.closed = False


def manhattan():
    puzzle = [7, 5, 0, 8, 6, 4, 2, 3, 1]
    startState = puzzleState(puzzle, calcManDis(puzzle), 0, calcManDis(puzzle))
    expansions = [startState]

    while True:
        expand(expansions)
        if checkSolvedMan(expansions):
            break


def checkSolvedMan(expansions):
    for x in expansions:
        if x.manDis == 0:
            print("Solved")
            print("States expanded: " + str(len(expansions)))
            return True
    return False


def expand(expansions):
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
        addNewState(expansions, stateIndex, puzzleDown)

    """Expand up"""
    if blankRow == 2 or blankRow == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 3]
        puzzleDown[blankIndex - 3] = 0
        addNewState(expansions, stateIndex, puzzleDown)

    """Expand left"""
    if blankColumn == 2 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex - 1]
        puzzleDown[blankIndex - 1] = 0
        addNewState(expansions, stateIndex, puzzleDown)

    """Expand right"""
    if blankColumn == 0 or blankColumn == 1:
        puzzleDown = copy.deepcopy(puzzle)
        puzzleDown[blankIndex] = puzzleDown[blankIndex + 1]
        puzzleDown[blankIndex + 1] = 0
        addNewState(expansions, stateIndex, puzzleDown)

    for x in expansions:
        if x.generation == expansions[stateIndex].generation:
            x.closed = True
    expansions[stateIndex].closed = True


def addNewState(expansions, stateIndex, puzzle):
    generation = expansions[stateIndex].generation + 1
    manDis = calcManDis(puzzle)
    newState = puzzleState(puzzle, manDis, generation, manDis + generation)
    if not checkDublicate(expansions, puzzle):
        expansions.append(newState)


def checkDublicate(expansions, puzzle):
    for x in expansions:
        if x.puzzle == puzzle:
            return True
    return False