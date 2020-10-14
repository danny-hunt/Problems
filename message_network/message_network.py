"""
A network consists of nodes labeled 0 to N.
You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node
to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
"""

import copy

N = 5
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5),
    (4, 1, 3)
]

# node = [label, current_lowest_time]
nodes = [[x, 1000] for x in range(N+1)]

first_edge_set = [edge for edge in edges if edge[0] == 0]
nodes[0] = [0, 0]


def get_next_edges(edge_set):
    new_edges = []
    for edge in edge_set:
        if edge[2] < nodes[edge[1]][1]:
            nodes[edge[1]][1] = edge[2]
            new_edges.extend(
                [(new_edge[0], new_edge[1], new_edge[2] + edge[2]) for new_edge in edges if new_edge[0] == edge[1]]
            )
    return new_edges


def repeat(edge_set):
    newest_edges = copy.copy(edge_set)
    while bool(newest_edges) is not False:
        newest_edges = get_next_edges(newest_edges)
    return nodes


calculated_nodes = repeat(first_edge_set)
print(calculated_nodes)
print(f'Maximum amount of time taken is {max([node[1] for node in calculated_nodes])}')








