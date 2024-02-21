from collections import Counter
from fileinput import filename
import time
from Node import path_actions
from EightPuzzle import valid_puzzle


# Max Timeout in Seconds, 15 minutes
MAX_TIMEOUT = 900

outputPath = "part3_output.txt"

class CountCalls:
    """Delegate all attribute gets to the object, and count them in ._counts"""
    def __init__(self, obj):
        self._object = obj
        self._counts = Counter()
        
    def __getattr__(self, attr):
        "Delegate to the original object, after incrementing a counter."
        self._counts[attr] += 1
        return getattr(self._object, attr)

        
def report(searchers, problems, verbose=True):
    """Show summary statistics for each searcher (and on each problem unless verbose is false)."""
    for searcher in searchers:
        print(searcher.__name__ + ':')
        total_counts = Counter()
        totalStartTime = time.time()
        numPuzzles = len(problems)
        for p in problems:
            fileName = p.fileName
            alg = p.alg
            problemName = str(p)[:40]
            problemStartTime = time.time()
            if not valid_puzzle(p):
                report_invalid(problemName, fileName)
                continue
            prob   = CountCalls(p)
            try:
                soln = searcher(prob)
            except:
                counts = prob._counts
                total_counts += counts
                report_timeout(problemName, counts['result'], fileName=fileName, alg=alg)
                continue
            problemEndTime = time.time()

            actions = ''
            for a in path_actions(soln):
                actions += str(a)

            counts = prob._counts
            counts.update(actions=len(soln), cost=soln.path_cost)
            total_counts += counts
            elapsedTime = problemEndTime - problemStartTime
            if verbose: report_counts(counts, problemName, elapsedTime, actions, fileName, alg)
        
        totalEndTime = time.time()
        report_counts(total_counts, 'TOTAL', totalEndTime - totalStartTime, actions, alg=alg, numPuzzles=numPuzzles)
         
def report_counts(counts, name, time, actions, fileName='', alg='', numPuzzles = None, numNodes = None):
    fileName_out = 'File: ' + fileName
    name_out = 'Problem: ' + name
    alg_out = 'Algorithm: ' + alg
    node_out = 'Nodes Generated: {:5,d}'.format(
          counts['result'])
    time_out = 'Time Taken: {:.6f} seconds'.format(
          time)
    path_length_out = 'Path Length: {:.0f}'.format(
          counts['cost'])
    path_out = 'Path: ' + actions
    lineBreak =  '--------------------------------------'
    total_out = 'TOTAL'

    avgTimePerPuzzle = ''
    avgNodesExplored = ''

    if name == 'TOTAL' and numPuzzles:
        avgTime = time / numPuzzles
        avgNodes = counts['result'] / numPuzzles

        avgTimePerPuzzle = 'Avg Run Time: ' + str(avgTime) + ' seconds'
        avgNodesExplored = 'Avg Nodes Explored: ' + str(avgNodes)
    

    individualLines = [fileName_out, name_out, alg_out, node_out, time_out, path_length_out, path_out, lineBreak]
    totalLines = [total_out, alg_out, node_out, time_out, avgTimePerPuzzle, avgNodesExplored, lineBreak]

    if name == 'TOTAL':
        for line in totalLines:
            print(line)

        writeToFile(totalLines, name)
    else:
        for line in individualLines:
            print(line)
        writeToFile(individualLines, name)



def report_timeout(name, nodesGenerated, fileName = '', alg = ''):
    fileName_out = 'File: ' + fileName
    name_out = 'Problem: ' + name
    alg_out = 'Algorithm: ' + alg
    node_out = 'Nodes Generated Before Timeout: {:5,d}'.format(
          nodesGenerated)
    exceed_time_out = 'Total time taken >15 minutes!'
    lineBreak =  '--------------------------------------'

    lines = [fileName_out, name_out, alg_out, node_out, exceed_time_out, lineBreak]

    for line in lines:
        print(line)

    writeToFile(lines, name)


def report_invalid(problemName, fileName):
    empty_out = ''
    cant_solve = 'Cannot Solve ' + fileName
    problemName = 'Problem: ' + problemName
    lineBreak =  '--------------------------------------'

    lines = [empty_out, cant_solve, problemName, lineBreak, empty_out]

    for line in lines:
        print(line)

    writeToFile(lines, problemName)


def writeToFile(lines, problemName):
    # Write to output.txt file
    linesToWrite = [line + '\n' for line in lines]
    writeFile = open(outputPath, 'a')
    writeFile.writelines(linesToWrite)
    writeFile.close()
