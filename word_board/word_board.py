"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

def exists(board, string):
    for i in len(board):
        for j in len(board[0]):
            word = string
            if board[i][j] == word[0]:
                route = [[i, j]]
                board[i][j] = '_'
                letter_index = 0
                letter_index += 1
                while word != '':
                    next_letter(i, j, word[letter_index:], board)

def next_letter(x, y, word, board):
    possible_positions = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    for position in possible_positions:
        if board[position[0]][position[1]] != word[0]:
            possible_positions.remove(position)
    if possible_positions != []:
        return possible_positions
    else:
        return False


word = "help"
for x in range(7):
    print(word[x:])