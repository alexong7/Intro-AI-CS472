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
        TicTacToe.__init__(self, h, v, k)