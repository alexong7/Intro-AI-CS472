# Question 6
For comparing the increase in depth and the result it has on the alphabeta agent,
I created a `metrics.py` file which gives reports on the # of states generated as well as the time it takes to finish.

```
def main():
    game = Gomoku(h=10, v=10)
    depth2_alphabeta = (h_alphabeta_search, cutoff_depth(2), evaluate_pattern, 'depth 2 alphabeta')
    depth3_alphabeta = (h_alphabeta_search, cutoff_depth(3), evaluate_pattern, 'depth 3 alphabeta')
    depth4_alphabeta = (h_alphabeta_search, cutoff_depth(4), evaluate_pattern, 'depth 4 alphabeta')
    depth5_alphabeta = (h_alphabeta_search, cutoff_depth(5), evaluate_pattern, 'depth 5 alphabeta')
    depth6_alphabeta = (h_alphabeta_search, cutoff_depth(6), evaluate_pattern, 'depth 6 alphabeta')

    report(game, (depth2_alphabeta, depth3_alphabeta, depth4_alphabeta, depth5_alphabeta, depth6_alphabeta))
```

Here we define multiple alphabeta agents that have the same evaluation function, `evalaute patterns`, which gets used in the event of a depth cutoff. The only parameter changed is the depth of the `cutoff` function.

# Results
```
Result states:     272;       Terminal tests:       0;       Total Time: 0.016915 seconds  for depth 2 alphabeta

Result states:   9,948;       Terminal tests:       0;       Total Time: 0.650659 seconds  for depth 3 alphabeta

Result states:  36,575;       Terminal tests:       0;       Total Time: 1.867427 seconds  for depth 4 alphabeta

Result states: 1,044,979;       Terminal tests:       0;       Total Time: 68.019834 seconds  for depth 5 alphabeta
```

Notice there is no terminal tests as this function only evaluates based off the initial state, an empty board. However, you can see the difference in how many states are generated for the first move based off of # of states generated, as well as time. 

`depth6_alphabeta` exceeded timeout, surpassing over 10 minutes at least before canceling.

There is tradeoff to having faster completion time. You get a more responsive agent, but it is not seeing far enough into the future to predict the best move all the time. It relies heavily on it's evaluation function in order to score the position of each possible move to ensure the best move is taken.