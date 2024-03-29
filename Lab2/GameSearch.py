import math
import functools

# This file defines the game search algorithms we 
# will use for playing the game.
#
# The Two include minimax and alphabeta (pruning) search
#
# Code from the AIMA-Python Github
# https://github.com/aimacode/aima-python/blob/master/games4e.ipynb


cache = functools.lru_cache(10**6)

def minimax_search(game, state):
    """Search game tree to determine best move; return (value, move) pair."""

    player = state.to_move

    def max_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a))
            if v2 < v:
                v, move = v2, a
        return v, move

    return max_value(state)

infinity = math.inf

def alphabeta_search(game, state):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -math.inf, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = math.inf, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, infinity)


# Minimax using a Transition Table (cache) to reduce duplicate paths
# Optimizes the search
def minimax_search_tt(game, state):
    """Search game to determine best move; return (value, move) pair."""

    player = state.to_move

    @cache
    def max_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    @cache
    def min_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a))
            if v2 < v:
                v, move = v2, a
        return v, move

    return max_value(state)

# Define our cache for alpha beta
def cache1(function):
    "Like lru_cache(None), but only considers the first argument of function."
    cache2 = {}
    def wrapped(x, *args):
        if x not in cache2:
            cache2[x] = function(x, *args)
        return cache2[x]
    return wrapped

# Alphabeta serach using a transition table (cache) for 
# optimization
def alphabeta_search_tt(game, state):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    @cache1
    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    @cache1
    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity)


def cutoff_depth(d):
    """A cutoff function that searches to depth d."""
    return lambda game, state, depth: depth > d

# Alphabeta with a cutoff_depth. Good for large boards with large
# game trees like Gomoku
def h_alphabeta_search(game, state, cutoff=cutoff_depth(1), h=lambda s, p: 0):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    def max_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta, depth+1)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity, 0)

# Evaluation Functions:
# ---------------------

# Evaluation function that gives a score based on the amount of 
# threats of the current state.
# A threat is where 4 in a row exists.
#
# The function will prioritize a chance to win if the player has 
# 4 in a row. Otherwise it will block the opponents 4 in a row
# if found.
def evaluate_threats(board, player):
    """
    Evaluate the current board state for the given player in terms of creating winning formations
    and blocking opponent threats.
    """
    # Define the opponent player
    opponent = 'O' if player == 'X' else 'X'

    # Initialize the threat score
    threat_score = 0

    # Check for winning opportunities for the player and potential threats from the opponent
    for line in rows(board) + columns(board) + diagonals(board):
        for i in range(len(line) - 4):
            # Check for winning formations for the player
            if line[i:i+5].count(player) == 4 and '.' in line[i:i+5]:
                threat_score += 100  # Prioritize completing player's winning sequences

            # Check for potential threats from the opponent
            elif line[i:i+5].count(opponent) == 4 and '.' in line[i:i+5]:
                threat_score -= 50  # Penalize opponent's potential winning sequences

    return threat_score


# Provides a score of the current board position
# based on common patterns in Gomoku, each weighted
# with a score
def evaluate_pattern(board, player):
    """
    Evaluate the current board state for the given player based on pattern recognition.
    """
    # Define the opponent player
    opponent = 'O' if player == 'X' else 'X'

    # Initialize the pattern score
    pattern_score = 0

    winning_patterns = [
        ('.' + player * 4, 100),                            # Make four in a row
        (player * 4 + '.', 100),                            # Make four in a row
        ('.' + player * 4 + '.', 200),                      # Open four in a row
        ('.' + player * 3 + '.', 5),                        # Open three
        ('.' + player * 2 + '.', 2),                        # Open two
        ('.' + opponent * 4 + '.', -800),                   # Threatened five by opponent
        ('.' + opponent * 3 + '.', -1000),                  # Threatened by opponent making a 4 with open ends
        ('.' + opponent + '.' + opponent * 2 + '.', -1000), # Threatened by opponent making a 4 with open ends
        ('.' + opponent + '.' + opponent * 2 + '.', -1000), # Threatened by opponent making a 4 with open ends
    ]

    # Check for each pattern ins rows, columns, and diagonals
    for line in rows(board) + columns(board) + diagonals(board):
        for pattern, score in winning_patterns:
            if pattern in ''.join(line):
                pattern_score += score
                
    return pattern_score


def rows(board):
    "Return a list of rows, each row is a list of cells."
    return [[board[x, y] for x in range(board.width)] for y in range(board.height)]

def columns(board):
    "Return a list of columns, each column is a list of cells."
    return [[board[x, y] for y in range(board.height)] for x in range(board.width)]

def diagonals(board):
    "Return a list of diagonals, each diagonal is a list of cells."
    return [[board[x+i, y+i] for i in range(board.width) if 0 <= x+i < board.width and 0 <= y+i < board.height] for x, y in [(0, y) for y in range(board.height)] + [(x, 0) for x in range(1, board.width)]]
    