from Game import *
from GameSearch import *
from TicTacToe import *
from Gomoku import *
from Player import *
import argparse


def main():
    parser=argparse.ArgumentParser()

    # Determine board size, will default to 15x15
    parser.add_argument("--width", help="Width of Board")
    parser.add_argument("--height", help="Height of Board")
    parser.add_argument("--eval", help="Evaluation function to use")
    parser.add_argument("--depth", help="Depth for the cutoff")
    parser.add_argument("--compare", action="store_true", help="Set this flag to True")

    args=parser.parse_args()

    width, height = 15, 15
    eval_fn = evaluate_pattern
    depth = 2

    if args.width != None and args.width != ""  and args.width.isdigit():
        width = int(args.width)
    
    if args.height != None and args.height != "" and args.height.isdigit():
        height = int(args.height)

    if args.depth != "" and args.depth != None and args.depth.isdigit():
        depth = int(args.depth)

    if args.eval != "" and args.eval != None:
        input = args.eval.lower()
        if input == 'threats':
            eval_fn = evaluate_threats
        if input == 'pattern':
            eval_fn = evaluate_pattern
    
    print(f'Using Evaluation Function: {"Pattern" if eval_fn == evaluate_pattern else "Threats"}')
    print(f'Using Cutoff Depth: {depth}')


    if args.compare:
        print('Comparing Evaluation Functions: Patterns vs Threats')
        compare_evaluation_functions(height, width)
    else:
        play_game(Gomoku(h=height, v=width), dict(X=user_player, O=h_alphabeta_search), verbose=True, eval_function=eval_fn, depth=depth).utility


def compare_evaluation_functions(height, width):
    """Play a turn-taking game. `strategies` is a {player_name: function} dict,
    where function(state, game) is used to get the player's move."""
    game = Gomoku(h=height, v=width)
    state = game.initial
    strategies=dict(
        X=(h_alphabeta_search, evaluate_pattern),
        O=(h_alphabeta_search, evaluate_threats)
    )
    while not game.is_terminal(state):
        player = state.to_move
        print(f'Turn {state.turn}')

        eval_function = strategies[player][1]

        # If we are using a cutoff, provide an evaluation function
        move = strategies[player][0](game, state, h=eval_function)
        state = game.result(state, move[1])

        print('Player', player, 'move:', move)
        print(state)
        
    print(f'Player {player} wins!')
    return state.utility
    



if __name__ == '__main__':
    main()
