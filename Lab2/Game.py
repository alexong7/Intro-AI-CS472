from GameSearch import *

# Abstract class for defining our Game
#
# Code from the AIMA-Python Github
# https://github.com/aimacode/aima-python/blob/master/games4e.ipynb
class Game:
    """A game is similar to a problem, but it has a terminal test instead of 
    a goal test, and a utility for each terminal state. To create a game, 
    subclass this class and implement `actions`, `result`, `is_terminal`, 
    and `utility`. You will also need to set the .initial attribute to the 
    initial state; this can be done in the constructor."""

    def actions(self, state):
        """Return a collection of the allowable moves from this state."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def is_terminal(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError
        

def play_game(game: Game, strategies: dict, verbose=False, eval_function=None, depth=3):
    """Play a turn-taking game. `strategies` is a {player_name: function} dict,
    where function(state, game) is used to get the player's move."""
    state = game.initial
    while not game.is_terminal(state):
        player = state.to_move
        print(f'Turn {state.turn}')

        strategy = strategies[player]

        # If we are using a cutoff, provide an evaluation function
        if strategies[player] == h_alphabeta_search:
            move = strategy(game, state, h=eval_function, cutoff=cutoff_depth(depth))
        else:
            move = strategy(game, state)


        if isinstance(move[1], tuple):
            state = game.result(state, move[1])
        else:
            state = game.result(state, move)
        if verbose: 
            print('Player', player, 'move:', move)
            print(state)
    print(f'Player {player} wins!')
    return state