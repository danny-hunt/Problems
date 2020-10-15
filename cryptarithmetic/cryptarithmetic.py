"""
A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters.
Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY

may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.
"""


def solve(operand_one, operand_two, result, operator = 'plus'):
    letter_list = []
    for letter in (operand_one + operand_two + result):
        if letter not in letter_list:
            letter_list.append(letter)
    assert len(letter_list) <= 10
    assert len(result) <= len(operand_two) + 1 and len(result) <= len(operand_one) + 1
    assert len(result) >= len(operand_two) and len(result) >= len(operand_one)
    while len(letter_list) < 10:
        letter_list.append('_')

    def calculate_number(string):
        number = 0
        power_ten = 0
        for letter in string[::-1]:
            number += letter_list.index(letter) * 10 ** power_ten
            power_ten += 1
        return number

    def fitness(operand_one, operand_two, result):
        first_number = calculate_number(operand_one)
        second_number = calculate_number(operand_two)
        resulting_number = calculate_number(result)

        sum = first_number + second_number





assert solve('SEND', 'MORE', 'MONEY') == ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

