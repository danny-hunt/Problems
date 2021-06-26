import numpy as np
import json
import pprint
import copy

with open('sudoku.json') as json_file:
    list_of_puzzles = json.load(json_file)['puzzle']

def solve(sudoku):
    return 5

def print_sudoku(board):
    board_for_printing = copy.copy(board)
    for index_r, row in enumerate(board_for_printing):
        for index_c, column in enumerate(row):
            if column == 0:
                board_for_printing[index_r][index_c] = ' '
    print('-' + '----'*9)
    for index, row in enumerate(board_for_printing):
        print(f'| {row[0]}   {row[1]}   {row[2]} | {row[3]}   {row[4]}   {row[5]} | {row[6]}   {row[7]}   {row[8]} |')
        if index % 3 == 2:
            print('|' + '-----------|'*3)
        else:
            print('|   +   +   '*3 + '|')


def check_solution(board):
    possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for row in board:
        for value in possible_values:
            if value not in row:
                return False
    return True


print(list_of_puzzles)
pprint.pprint(list_of_puzzles[0])
print_sudoku(list_of_puzzles[0])
print(check_solution(list_of_puzzles[0]))
