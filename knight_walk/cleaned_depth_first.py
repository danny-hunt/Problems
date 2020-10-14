"""
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""
import copy
from time import time

import cProfile
import pstats
import io

# Assume that the board has a coordinate system and that tours sharing symmetry with other tours are still unique
N = 4
knight_movements = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]


def create_board(n):
    board = list()
    for _ in range(n):
        board.append([0] * n)
    return board


board = create_board(N)
print(board)


def knights_moves(board, position):
    possible_moves = list()
    for movement in knight_movements:
        new_x = movement[0] + position[0]
        new_y = movement[1] + position[1]
        if 0 <= new_x < N and 0 <= new_y < N:
            if board[new_x][new_y] == 0:
                possible_moves.append((new_x, new_y))
    return possible_moves


# print(knights_moves(board, [2,2]))


def knights_tours(board, starting_square, count=0):
    count = 0
    boardcopy = copy.deepcopy(board)
    boardcopy[starting_square[0]][starting_square[1]] = 1
    if knights_moves(boardcopy, starting_square) != []:
        for move in knights_moves(boardcopy, starting_square):
            # print(move)
            # boardcopy = board.copy()
            # boardcopy.remove(move)
            count += knights_tours(boardcopy, move)
    elif boardcopy == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
        # print("knight's path!")
        count += 1
    return count


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    start = time()
    tours = 0
    for x in range(N):
        for y in range(N):
            starting_square = (x,y)
            square_start = time()
            square_tours = knights_tours(board, starting_square)
            tours += square_tours
            print(f'square = {starting_square} and the number of tours is {square_tours}')
            end = time()
            print(f'It took {end-square_start} seconds')
    print(f'Total tours = {tours}')
    end = time()
    print(f'It took {end-start} seconds')

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('cleaned_profile.txt', 'w+') as f:
        f.write(s.getvalue())


"""
Output for N = 5:
square = [1, 1] and the number of tours is 304
square = [1, 2] and the number of tours is 0
square = [1, 3] and the number of tours is 56
square = [1, 4] and the number of tours is 0
square = [1, 5] and the number of tours is 304
square = [2, 1] and the number of tours is 0
square = [2, 2] and the number of tours is 56
square = [2, 3] and the number of tours is 0
square = [2, 4] and the number of tours is 56
square = [2, 5] and the number of tours is 0
square = [3, 1] and the number of tours is 56
square = [3, 2] and the number of tours is 0
square = [3, 3] and the number of tours is 64
square = [3, 4] and the number of tours is 0
square = [3, 5] and the number of tours is 56
square = [4, 1] and the number of tours is 0
square = [4, 2] and the number of tours is 56
square = [4, 3] and the number of tours is 0
square = [4, 4] and the number of tours is 56
square = [4, 5] and the number of tours is 0
square = [5, 1] and the number of tours is 304
square = [5, 2] and the number of tours is 0
square = [5, 3] and the number of tours is 56
square = [5, 4] and the number of tours is 0
square = [5, 5] and the number of tours is 304
Total tours = 1728
It took 966.2659137248993 seconds
"""