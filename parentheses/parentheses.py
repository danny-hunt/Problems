"""
Given a string of parentheses,
write a function to compute the minimum number of parentheses to be removed
to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""

"""
) <-- always removed
 ((()(()
01232343

"""


def count_removal(parentheses):
    levels_deep = 0
    backwards_facing_removed = 0
    for parenthesis in parentheses:
        if parenthesis == "(":
            levels_deep += 1
        elif parenthesis == ")":
            if levels_deep == 0:
                backwards_facing_removed += 1
            else:
                levels_deep -= 1
    return levels_deep + backwards_facing_removed

test_string = ")(("
assert count_removal(test_string) == 3
another_test_string = "()))()()((()()((((()()()()))))))"
assert count_removal(another_test_string) == 2

