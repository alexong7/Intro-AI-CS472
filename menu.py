from puzzler import *
from puzzleGenerator import *


def startMenu():
    print("(1)  Solve 1 Puzzle using Manhattan")
    print("(2)  Solve 1 Puzzle using Hamming")
    print("(3)  Solve 100 Puzzles using Manhattan")
    print("(4)  Solve 100 Puzzles using Hamming")
    print("(5)  Exit" + "\n")

    """
    Main menu with 5 options to solve 1 or 100 puzzles using either Manhattan or Hamming heuristic.
    
    Option 1, 2: hamming() or manhattan() from puzzler.py are called with 1 puzzle.
    Option 3, 4: puzzles object is created with create100Variations() from puzzleGenerator.py.
    
    manhattan() and hamming() from puzzler.py return statistics on the heuristic's time complexity 
    (execution time), and space complexity, i.e. memory usage (required steps, expanded nodes). 
    Stats are printed to the console.
    """

    option = 0
    while option < 1 or option > 5:
        try:
            option = int(input("Choose Option: "))
        except ValueError as ve:
            print("Please enter a number!")

        if option == 1:
            print("\n" + "Manhattan (x1)")
            printStats(manhattan(create100Variations()[0]))
        elif option == 2:
            print("\n" + "Hamming (x1)")
            printStats(hamming(create100Variations()[0]))
        elif option == 3:
            puzzles = create100Variations()
            stats = []
            for x in puzzles:
                stats.append(manhattan(x))
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 49:
                    print()
            print("\n" + "Manhattan (x100)")
            printTotalStats(stats)
        elif option == 4:
            puzzles = create100Variations()
            stats = []
            for x in puzzles:
                stats.append(hamming(x))
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 49:
                    print()
            print("\n" + "Hamming (x100)")
            printTotalStats(stats)
        elif option == 5:
            quit()

    proceed = input("Press enter to continue." + "\n")
    startMenu()

    """
    Methods printStats() for single runs and printTotalStats() for 100x runs.
    
    Input: stats (time, steps, expanded nodes)
    Output: stats printed to console
    """

def printStats(stats):
    print("Expansions: " + str(stats.expansions))
    print("Steps: " + str(stats.steps))
    print("Time taken: " + str(round(stats.time, 3)))
    print()


def printTotalStats(stats):
    expansions = 0
    steps = 0
    time = 0
    expansionsList = []
    stepsList = []
    timeList = []

    """
    Summing up the values
    """

    for x in stats:
        expansions += x.expansions
        steps += x.steps
        time += x.time
        expansionsList.append(x.expansions)
        stepsList.append(x.steps)
        timeList.append(x.time)

    """
    Calculation of mean deviation
    """

    expansionsMean = expansions / 100
    stepsMean = steps / 100
    timeMean = time / 100

    """
    Calculation of standard deviation
    """

    expansionsSD = 0
    stepsSD = 0
    timeSD = 0
    for i in range(100):
        expansionsList[i] = math.pow((expansionsList[i] - expansionsMean), 2)
        expansionsSD += expansionsList[i]
        stepsList[i] = math.pow((stepsList[i] - stepsMean), 2)
        stepsSD += stepsList[i]
        timeList[i] = math.pow((timeList[i] - timeMean), 2)
        timeSD += timeList[i]

    expansionsSD = math.sqrt(expansionsSD / 99)
    stepsSD = math.sqrt(stepsSD / 99)
    timeSD = math.sqrt(timeSD / 99)

    print("Expansions [total/mean deviation]: " + str(expansions) + " / " + str(expansionsMean))
    print("Steps [total/mean deviation]: " + str(steps) + " / " + str(stepsMean))
    print("Time [total/mean deviation]: " + str(round(time, 3)) + " / " + str(round(timeMean, 3)))
    print()
    print("Expansions standard deviation: " + str(round(expansionsSD, 3)))
    print("Steps standard deviation: " + str(round(stepsSD, 3)))
    print("Time standard deviation: " + str(round(timeSD, 3)))
    print()
