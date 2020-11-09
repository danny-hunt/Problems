"""
You are given a starting state start, a list of transition probabilities for a Markov chain,
and a number of steps num_steps. Run the Markov chain starting from start for num_steps and
compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

import random

transition_probabilities = [
    [0.9, 0.075, 0.025],
    [0.15, 0.8, 0.05],
    [0.25, 0.25, 0.5]
]

transition_cum_probabilities = [
    [0.9, 0.975, 1],
    [0.15, 0.95, 1],
    [0.25, 0.5, 1]
]

letter_to_index = {"a": 0, "b": 1, "c": 2}


def count_visits(starting_state, num_steps):
    currently_at = starting_state
    visit_tally = {"a": 0, "b": 0, "c": 0}
    visit_tally[currently_at] += 1

    for _ in range(num_steps):
        rand = random.random()
        if rand < transition_cum_probabilities[letter_to_index[currently_at]][0]:
            visit_tally["a"] += 1
            currently_at = "a"
        elif rand < transition_cum_probabilities[letter_to_index[currently_at]][1]:
            visit_tally["b"] += 1
            currently_at = "b"
        else:
            visit_tally["c"] += 1
            currently_at = "c"

    return visit_tally

print(count_visits("a", 5000))


