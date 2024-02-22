
from Problem import * 
import numpy as np



# Code from the AIMA book
class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank, trying to reach a goal configuration.
    A board state is represented as a tuple of length 9, where the element at index i 
    represents the tile number at index i, or 0 if for the empty square, e.g. the goal:
        1 2 3
        4 5 6 ==> (1, 2, 3, 4, 5, 6, 7, 8, 0)
        7 8 _
    """

    def __init__(self, initial, alg=None, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0), fileName = ''):
        super().__init__(initial, goal)
        self.initial, self.alg, self.goal = initial, alg, goal
        self.fileName = fileName

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['U', 'D', 'L', 'R']
        index_blank_square = state.index(0)

        if index_blank_square % 3 == 0:
            possible_actions.remove('L')
        if index_blank_square < 3:
            possible_actions.remove('U')
        if index_blank_square % 3 == 2:
            possible_actions.remove('R')
        if index_blank_square > 5:
            possible_actions.remove('D')

        return possible_actions
    
    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = state.index(0)
        new_state = list(state)

        delta = {'U': -3, 'D': 3, 'L': -1, 'R': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    # Define which heuristic, if any, to use
    def h(self, node): 
        if self.alg == 'h1':
            return self.h1(node)
        if self.alg == 'h2':
            return self.h2(node)
        if self.alg == 'h3':
            return self.h3(node)
        
        return 0
    
    # Hamming Distance
    def h1(self, node):
        return hamming_distance(node.state, self.goal)
        
    # Mannhatten Distance
    def h2(self, node):
        X = (0, 1, 2, 0, 1, 2, 0, 1, 2)
        Y = (0, 0, 0, 1, 1, 1, 2, 2, 2)
        return sum(abs(X[s] - X[g]) + abs(Y[s] - Y[g])
                    for (s, g) in zip(node.state, self.goal) if s != 0)
        
    # Heuristic using Euclidean Distance
    def h3(self, node):
        return euclidean_distance(node.state, self.goal)



    
def hamming_distance(A, B):
    "Number of positions where vectors A and B are different."
    return sum(a != b for a, b in zip(A, B))

def euclidean_distance(x, y):
    return np.sqrt(sum((_x - _y) ** 2 for _x, _y in zip(x, y)))

def valid_puzzle(state):
    return inversions(state.initial) % 2 == inversions((1, 2, 3, 4, 5, 6, 7, 8, 0)) % 2 


def inversions(board):
    "The number of times a piece is a smaller number than a following piece."
    return sum((a > b and a != 0 and b != 0) for (a, b) in combinations(board, 2))
    
    
def board8(board, fmt=(3 * '{} {} {}\n')):
    "A string representing an 8-puzzle board"
    return fmt.format(*board).replace('0', '_')

class Board(defaultdict):
    empty = '.'
    off = '#'
    def __init__(self, board=None, width=8, height=8, to_move=None, **kwds):
        if board is not None:
            self.update(board)
            self.width, self.height = (board.width, board.height) 
        else:
            self.width, self.height = (width, height)
        self.to_move = to_move

    def __missing__(self, key):
        x, y = key
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.off
        else:
            return self.empty
        
    def __repr__(self):
        def row(y): return ' '.join(self[x, y] for x in range(self.width))
        return '\n'.join(row(y) for y in range(self.height))
            
    def __hash__(self): 
        return hash(tuple(sorted(self.items()))) + hash(self.to_move)