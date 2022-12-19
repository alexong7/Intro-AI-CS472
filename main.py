import time
import random
from colorama import Fore, Back, Style

from puzzleGenerator import *
from manhatten import *
from hemming import *
from puzzler import *

if __name__ == '__main__':

    a100Puzzles = create100Variations()
    #print(a100Puzzles)

    #drawPuzzleStart(a100Puzzles[0])

    manhattan()