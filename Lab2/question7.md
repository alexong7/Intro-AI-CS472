# Question 7
For my two evaluation functions, I have created one called `evaluate_threats` and the other `evaluate_patterns`.

## Evaluate Threats
Evaluate threats acts as more of a defensive evaluation function, which 
prioritizes blocking any chances for an opponent to win the game.

It will prioritize winning as well if given the chance
```
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
```

## Evaluate Patterns
This one is arguably more balanced and better performing. Evaluate pattern accounts for common "winning" or "losing" patterns and assigns a score weight to each position. This way, it can play a balanced offense and defense, by building up to a chance to make 5 in a row, but can also see in advance if an opponent is setting the board up to make any moves that could result in a checkmate, where a win is guaranteed.

I personally enjoyed this evaluation function more, as I could add more patterns to be recognized as I played, which allows the agent to be smarter with counter play.

```
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
```

# Comparison
I played the game creating two agents using alpha beta search with a cutoff, and gave each one either evaluate threats or evaluate patterns as the evaluation function.

In all scenarios, I ran the game > 30 times and found that `evaluate_patterns` won each time as it was able to play both a stronger offense and defense, while threats only prioritized defense, but could not see checkmate making moves:

`Ex: .XX.X. where adding an X to make .XXXX. makes an open ended 4 in a row, meaning the next turn is a guaranteed win.`

```
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
```

# How to Compare
Use the `--compare` flag to run the two evaluation functions against each other instead of playing as a user
Ex: with width/height changes (10x10 runs faster than 15x15)

`python3 main.py --width 10 --height 10 --compare`