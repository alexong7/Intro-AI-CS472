from TicTacToe import *

# This file defines the Gomoku game which
# is just an extension of TicTacToe, but on a
# bigger board and an win condition of 5 in a row
#
# Code from the AIMA-Python Github
# https://github.com/aimacode/aima-python/blob/master/games.py
class Gomoku(TicTacToe):
    """Also known as Five in a row."""

    def __init__(self, h=15, v=15, k=5):
        centerX, centerY = (h - 1) // 2, (v - 1) // 2
        self.center = (centerX, centerY)
        self.centerBoundary = {(x, y) for x in range(centerX - 2, centerX + 3) for y in range(centerY - 2, centerY + 3)}

        TicTacToe.__init__(self, h, v, k)

    # Gomoku checks for turns 1 and 3 for constraints, otherwise
    # uses Tic Tac Toe actions, which is just any available spot on
    # the board
    def actions(self, board):
        if board.turn == 1:
            return {self.center}
        if board.turn == 3:
            return self.squares - self.centerBoundary - set(board)
        return TicTacToe.actions(self, board)