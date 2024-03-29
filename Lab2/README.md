# CS472 Lab 2
This folder contains the code to play Gomoku against an AI search agent that uses `alphabeta` search and two different possible evaluation functions in the event of a cutoff for large search trees.

The game is played and printed on the console.

## How to Run
Main Script `python3 main.py`

Takes a user input in the form of `int , int` <br/>
Two ints separated by a comma. Must follow opening rules and be within bounds.<br/>
1st move of First player has to be center (game will tell you)<br/>
2nd move of First player has to be 2 intersections away from first move<br>

## Recommendations
The game plays better on a smaller board, giving faster decisions.
`10x10` is best recommended, with a `--depth` of 2 or 3

## Flags
`--width` : Width of Board. Default `15` 

`--height` : Height of Board. Default `15`

`--eval`: Evaluation Function to use: (see `question7.md` for more detail)
- `pattern`: Evaluates using common winning patterns 
- `threats`: Evaluates looking for winning or losing threats
- Defaults to `pattern`

`--depth`: Cutoff depth to use: Default `2`

`--compare`: Boolean flag, by using this you don't play against an agent, you compare two evaluation functions by having two `alphabeta` search agents play each other. One has `evaluate_threats` and the other has `evaluate_pattern` as the evaluation functions.

# Examples
Default:<br/>
15x15 board <br/>
Cutoff Depth 2 <br/>
Eval Function: Pattern
`python3 main.py`


10x10 Board <br/>
Cutoff depth 3 <br/>
Eval Function: pattern <br/>
`python3 main.py --height 10 --width 10 --depth 3 --eval pattern`

9x9 Board <br/>
Cutoff depth 4 <br/>
Eval Function: threats <br/>
`python3 main.py --height 9 --width 9 --depth 4 --eval threats`


Compare: Watch the two eval function AIs play each other: <br/>
`python3 main.py --height 10 --width 10 --compare`

# Code Structure

### Game.py
- Game Interface
- Defines `play_game`, the main driving code of playing turns and updating the board

### TicTacToe.py & Gomoku.py
- Implementations of `Game`. 
- Gomoku extends TicTacToe, larger board and aims for 5 in a row
- The state is the `Board` which is defined here. 
- Defines all possible moves and checks for wins

### GameSearch.py
- All the search functions for `alphabeta`, as well as extra `minmax` and versions of these with caches
- Has the two evaluation functions `evaluate_patterns` and `evaluate_threats`

### Player.py
- Defines the either the user agent, which just waits for user input
- The random player which picks random moves
- Or the search player, which takes in a search function and state and uses those to pick the best move

### Metrics.py
- Used for examining metrics like number of state generated or time to run a game search for a turn