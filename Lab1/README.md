# Lab 1 - Alex Ong

## How to Run
The entry point for this code is in the `main.py` file. The program expects two command line arguments `--fPath` and `--alg`, where it defines the File Path or Directory, and the algorithm to solve against respectively.

`--fPath` can take either a path to a single file, or to a directory. If the argument is a directory, it will run against each file in the directory (useful for Part 2 and 3).

`--alg` can be a value of either:
- `bfs`
- `ids`
- `h1`
- `h2`
- `h3`

# Examples of running the application:

### Run all puzzles in a directory against bfs
`python3 main.py --fPath Part2 --alg bfs`

### Run a single puzzle against h2
`python3 main.py --fPath Part2/S1.txt --alg h2`


The outputs will be printed to the console, as well as written to the file specifed in the `metrics.py` file. 

# Outputs explained
The outputs for Part 2 and Part 3 can be found in a few areas.

`part2_output.txt` will show all five puzzles in the Part2 folder ran against all 5 algorithms (25 in total).

This will display the optimal solutions, time, nodes generated, solution path, and averages for the entire run.

### Example

```
Breath First Search Part 2:
----------------------------------------
File: S4.txt
Problem: EightPuzzle((8, 6, 7, 2, 5, 4, 3, 0, 1),
Algorithm: bfs
Nodes Generated: 483,563
Time Taken: 4.168279 seconds
Path Length: 31
Path: UULDDRRUULDLDRRUULDLDRRUULLDDRR


...

Cannot Solve S3.txt
Problem: EightPuzzle((7, 5, 2, 6, 3, 1, 4, 8, 0),
--------------------------------------

...

IDS Part 2:
-------------------------------------
File: S4.txt
Problem: EightPuzzle((8, 6, 7, 2, 5, 4, 3, 0, 1),
Algorithm: ids
Nodes Generated Before Timeout: 69,692,609
Total time taken >15 minutes!
--------------------------------------
```

## Part 3
`part3_output.txt` has all 60 puzzles ran against all 5 search algorithms with the same outputs as above, resulting in 300 total outputs.

`part3_table.png` shows an image of the results table, showing the average run time and average nodes generated for each algorithm in the L8, L15, and L24 test cases. 

`part3_conclusions.txt` goes into detail about my conclusions and final thoughts regarding the findings from Part 3


# File Breakdown
A majority of the code was grabbed from the AIMA Github 
https://github.com/aimacode/aima-python

`metrics.py` is resposible for a majority of the driver of the program. It will take in a search algorithm and a list of puzzles to solve with that algorithm in the `report()` function, then will both output to the console via print statements, and write the same outputs to a text file

`main.py` is the entry to input the command line arguments

`Search_Algorithms` defines all the search algorithms used

`EightPuzzle.py` is a subclass of `Puzzle.py` and defines all the actions and expansion rules as well as heuristics for each puzzle