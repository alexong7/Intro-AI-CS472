from Game import *
from GameSearch import *
from TicTacToe import *
from Gomoku import *


def main():
    play_game(Gomoku(), dict(X=player(h_alphabeta_search), O=random_player), verbose=True).utility
    # play_game(Gomoku(), dict(X=random_player, O=random_player), verbose=True).utility




if __name__ == '__main__':
    main()
