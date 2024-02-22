from mimetypes import init
import sys
import argparse
import os

from EightPuzzle import *
from Node import *
from Search_Algorithms import *
import time
from metrics import *


def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--fPath", help="File path for puzzle")
    parser.add_argument("--alg", help="Search algorithm to run")

    args=parser.parse_args()

    if args.fPath == "" or args.alg == "":
        print("Empty Arguments")
        sys.exit()

    algStr = args.alg.lower()
    alg = None

    if algStr == 'bfs':
        alg = breadth_first_search
    elif algStr == 'ids':
        alg = iterative_deepening_search
    elif algStr == 'h1':
        alg = astar_search
        print('Using h1')
    elif algStr == 'h2':
        alg = astar_search
        print('Using h2')
    elif algStr == 'h3':
        alg = astar_search
        print('Using h3')
    else:
        print("Enter a valid Algorithm: bfs -- ids -- h1 -- h2 -- h3")
        sys.exit()

    # if algStr not in ['h1', 'h2', 'h3']:
    #     algStr = None

    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, args.fPath)

    isDirectory = os.path.isdir(file_name)
    isFile = os.path.isfile(file_name)

    # Scan and parse all puzzles
    puzzles = []
    if isDirectory: 
        for file in os.listdir(file_name):
            filePath = os.path.join(file_dir, file_name + "/" + file)
            initialBoard = parseBoard(filePath)
            puzzles.append(EightPuzzle(initialBoard, alg = algStr, fileName=file))

    elif isFile:
            initialBoard = parseBoard(file_name)
            puzzles.append(EightPuzzle(initialBoard, alg = algStr, fileName=file_name.split('/')[-1]))
    else:
        print("Bad File Path")
        sys.exit()

    
    # e1 = EightPuzzle((5, 3, 1, 0, 8, 7, 2, 6, 4))



    report([alg], puzzles)
 


def parseBoard(filePath):
    file = open(filePath, "r")
    lines = file.readlines()

    temp = []
    for line in lines:
        temp.extend(line.replace("\n", "").replace("_", "0").split(' '))
    file.close()

    return tuple(list(map(int, temp))
)
    
if __name__ == '__main__':
    main()

