"""
Given a 2D matrix of characters and a target word,
write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

def find_word(word, grid):
    y_dim = len(grid)
    x_dim = len(grid[0])

    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter == word[0]:
                is_horizontal = True
                is_vertical = True
                x_pos = x
                y_pos = y
                for character in word:
                    if character != grid[y_pos][x_pos]:
                        is_horizontal = False
                        break
                    x_pos += 1

                x_pos = x
                y_pos = y
                for character in word:
                    if character != grid[y_pos][x_pos]:
                        is_vertical = False
                        break
                    y_pos += 1

                if is_horizontal:
                    return True
                if is_vertical:
                    return True

    return False

print(find_word("FOAM", [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]))

print(find_word("FACT", [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]))