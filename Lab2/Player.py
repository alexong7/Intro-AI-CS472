import random

# Defines our player types
#
# We have a random player which picks random moves
# We have a player that takes plays based off a specific search algorithm
# And a user player which defines options for user input 
def random_player(game, state): return random.choice(list(game.actions(state)))

def player(search_algorithm):
    """A game player who uses the specified search algorithm"""
    return lambda game, state: search_algorithm(game, state)[1]

def user_player(game, state):
    validMove = False

    while not validMove:
        if(state.turn == 1):
            print(f'Note: Turn 1 must be in the center: {game.center}')
        userInput = input('Your Turn (Takes two integers in the form "X,Y" separated by a ","): ')
        values = userInput.split(',')

        if len(values) != 2:
            print(f'Malformed Input: {values}\n')
            continue

        x = values[0].strip()
        y = values[1].strip()

        if not x.isdigit() or not y.isdigit():
            print('Enter valid numbers\n')
            continue

        move = (int(x), int(y))

        if move not in game.actions(state):
            print(f'Invalid Move {move}, Try again\n')
            continue
        
        return move
