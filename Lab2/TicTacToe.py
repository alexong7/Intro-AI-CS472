from Game import *
from collections import defaultdict


# We define a simple Tic Tac Toe game in 
# order to build off into our Gomoku game.
#
# Gomoku is essentially a larger board version of 
# Tic Tac Toe and aims for 5 in a row connections.
#
# Code used from the AIMA-Python Github
# https://github.com/aimacode/aima-python/blob/master/games4e.ipynb

class TicTacToe(Game):
    """Play TicTacToe on an `height` by `width` board, needing `k` in a row to win.
    'X' plays first against 'O'."""

    def __init__(self, height=3, width=3, k=3):
        self.k = k # k in a row
        self.squares = {(x, y) for x in range(width) for y in range(height)}
        self.initial = Board(height=height, width=width, to_move='X', utility=0)

    def actions(self, board):
        """Legal moves are any square not yet taken."""
        return self.squares - set(board)

    def result(self, board, square):
        """Place a marker for current player on square."""
        player = board.to_move
        board = board.new({square: player}, to_move=('O' if player == 'X' else 'X'), turn = board.turn + 1)
        win = k_in_row(board, player, square, self.k)
        board.utility = (0 if not win else +5000 if player == 'X' else -5000)
        return board

    def utility(self, board, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return board.utility if player == 'X' else -board.utility

    def is_terminal(self, board):
        """A board is a terminal state if it is won or there are no empty squares."""
        return board.utility != 0 or len(self.squares) == len(board)

    def display(self, board): print(board)     


def k_in_row(board, player, square, k):
    """True if player has k pieces in a line through square."""
    def in_row(x, y, dx, dy): return 0 if board[x, y] != player else 1 + in_row(x + dx, y + dy, dx, dy)
    return any(in_row(*square, dx, dy) + in_row(*square, -dx, -dy) - 1 >= k
               for (dx, dy) in ((0, 1), (1, 0), (1, 1), (1, -1)))


class Board(defaultdict):
    """A board has the player to move, a cached utility value, 
    and a dict of {(x, y): player} entries, where player is 'X' or 'O'."""
    empty = '.'
    off = '#'
    
    def __init__(self, width=8, height=8, to_move=None, turn=1, **kwds):
        self.__dict__.update(width=width, height=height, to_move=to_move, turn=turn, **kwds)
        self.width, self.height = width, height
        self.to_move = to_move
        self.turn = turn

        
    def new(self, changes: dict, **kwds) -> 'Board':
        "Given a dict of {(x, y): contents} changes, return a new Board with the changes."
        board = Board(width=self.width, height=self.height, **kwds)
        board.update(self)
        board.update(changes)
        return board

    def __missing__(self, loc):
        x, y = loc
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.empty
        else:
            return self.off
            
    def __hash__(self): 
        return hash(tuple(sorted(self.items()))) + hash(self.to_move)
    

    def __repr__(self):
        def row(y):
            # Include row number
            row_label = str(y).rjust(2) + ' '
            # Join cells in the row with spaces and adjust spacing for alignment
            row_content = ' '.join(self[x, y].center(3) for x in range(self.width))
            return row_label + row_content

        # Create column labels with adjusted spacing
        col_labels = '   ' + ' '.join(str(i).center(3) for i in range(self.width))

        # Join rows with line breaks and add column labels at the top
        return col_labels + '\n' + '\n'.join(map(row, range(self.height))) + '\n'
        
