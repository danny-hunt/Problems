"""
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order.
Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends",
meaning that if you turn the wheels to one of these combinations,
the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction.
Given a lock initially set to 000, a target combination, and a list of dead ends,
write a function that returns the minimum number of moves required to reach the target state,
or None if this is impossible.
"""


def dijkstra(target, dead_ends, start=(0,0,0)):
    vertex_set = {(i, j, k) for i in range(10) for j in range(10) for k in range(10)}
    distances = {v: 10000 for v in vertex_set}
    distances[start] = 0
    counter = 0
    while distances:
        nearest_vertex = min(distances, key=distances.get)

        for neighbour in neighbours(nearest_vertex):
            if neighbour in distances:
                alternative = distances[nearest_vertex] + 1000 if neighbour in dead_ends else distances[nearest_vertex] + 1
                if alternative < distances[neighbour]:
                    distances[neighbour] = alternative

        if nearest_vertex == target:
            if distances[target] < 1000:
                return distances[target], counter
            else:
                return None, counter

        del distances[nearest_vertex]
        counter += 1


def neighbours(vertex):
    return {((vertex[0] + 1) % 10, vertex[1], vertex[2]),
                     ((vertex[0] - 1) % 10, vertex[1], vertex[2]),
                     (vertex[0], (vertex[1] + 1) % 10, vertex[2]),
                     (vertex[0], (vertex[1] - 1) % 10, vertex[2]),
                     (vertex[0], vertex[1], (vertex[2] + 1) % 10),
                     (vertex[0], vertex[1], (vertex[2] - 1) % 10)}


assert dijkstra((0, 0, 2), [(0, 0, 1)])[0] == 4
assert not dijkstra((0, 0, 2), neighbours((0, 0, 2)))[0]
print(dijkstra((0, 0, 2), neighbours((0, 0, 2))))
print(dijkstra((5, 5, 5), {}))


