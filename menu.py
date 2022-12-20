from puzzler import *
from puzzleGenerator import *


def startMenu():
    print("Menu" + "\n")
    print("(1)  Solve 1 Puzzle using Manhattan")
    print("(2)  Solve 1 Puzzle using Hamming")
    print("(3)  Solve 100 Puzzles using Manhattan")
    print("(4)  Solve 100 Puzzles using Hamming")
    print("(5)  Exit" + "\n")

    """main menu with 5 options to solve 1 or 100 puzzles using either manhattan or hamming.
    manhattan() and hamming() return statistics about the execution which are printed below"""

    option = 0
    while option < 1 or option > 5:
        try:
            option = int(input("Choose Option: "))
        except ValueError as ve:
            print("Please enter a number!")

        if option == 1:
            print("\n" + "Manhatten (x1)")
            printStats(manhattan(create100Variations()[0]))
        elif option == 2:
            print("\n" + "Hamming (x1)")
            printStats(hamming(create100Variations()[0]))
        elif option == 3:
            puzzles = create100Variations()
            totalExpansions = 0
            totalTime = 0
            totalSteps = 0
            for x in puzzles:
                stats = manhattan(x)
                totalExpansions += stats.expansions
                totalTime += stats.time
                totalSteps += stats.steps
                print(puzzles.index(x))
            print("\n" + "Manhatten (x100)")
            printTotalStats([totalExpansions, totalTime, totalSteps])
        elif option == 4:
            puzzles = create100Variations()
            totalExpansions = 0
            totalTime = 0
            totalSteps = 0
            for x in puzzles:
                stats = hamming(x)
                totalExpansions += stats.expansions
                totalTime += stats.time
                totalSteps += stats.steps
                print(puzzles.index(x))
            print("\n" + "Hamming (x100)")
            printTotalStats([totalExpansions, totalTime, totalSteps])
        elif option == 5:
            quit()

    proceed = input("Press enter key to continue." + "\n")
    startMenu()


    """printing single runs and 100x runs.
    
    Input: stats (time, steps, expanded nodes).
    Output: print to console"""

def printStats(stats):
    print("Expansions: " + str(stats.expansions))
    print("Steps: " + str(stats.steps))
    print("Time taken: " + str(round(stats.time, 3)))
    print()


def printTotalStats(stats):
    print("Expansions [total/avg.]: " + str(stats[0]) + " / " + str(stats[0] / 100))
    print("Steps [total/avg.]: " + str(stats[2]) + " / " + str(stats[2] / 100))
    print("Time [total/avg.]: " + str(round(stats[1], 3)) + " / " + str(round(stats[1] / 100, 3)))
    print()