
from collections import Counter
from Gomoku import *
import time

# Ways to evaluate the game search algorithms
#
# Code from the AIMA-Python Github
# https://github.com/aimacode/aima-python/blob/master/games4e.ipynb

class CountCalls:
    """Delegate all attribute gets to the object, and count them in ._counts"""
    def __init__(self, obj):
        self._object = obj
        self._counts = Counter()
        
    def __getattr__(self, attr):
        "Delegate to the original object, after incrementing a counter."
        self._counts[attr] += 1
        return getattr(self._object, attr)
    
def report(game, searchers):
    for searcher in searchers:
        game = CountCalls(game)
        # searcher(game, game.initial)
        startTime = time.time()
        searcher[0](game, game.initial, cutoff=searcher[1], h=searcher[2])
        endTime = time.time()
        print('Result states: {:7,d};       Terminal tests: {:7,d};       Total Time: {:.6f} seconds  for {}'.format(
            game._counts['result'], game._counts['terminalCount'], endTime - startTime, searcher[3]))
        

def main():
    game = Gomoku(h=10, v=10)
    depth2_alphabeta = (h_alphabeta_search, cutoff_depth(2), evaluate_pattern, 'depth 2 alphabeta')
    depth3_alphabeta = (h_alphabeta_search, cutoff_depth(3), evaluate_pattern, 'depth 3 alphabeta')
    depth4_alphabeta = (h_alphabeta_search, cutoff_depth(4), evaluate_pattern, 'depth 4 alphabeta')
    depth5_alphabeta = (h_alphabeta_search, cutoff_depth(5), evaluate_pattern, 'depth 5 alphabeta')
    depth6_alphabeta = (h_alphabeta_search, cutoff_depth(6), evaluate_pattern, 'depth 6 alphabeta')

    report(game, (depth2_alphabeta, depth3_alphabeta, depth4_alphabeta, depth5_alphabeta, depth6_alphabeta))



if __name__ == '__main__':
    main()
