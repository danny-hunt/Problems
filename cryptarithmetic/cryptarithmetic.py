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
import random
import copy


def solve(operand_one, operand_two, result, operator = 'plus'):
    input_data = [operand_one, operand_two, result]
    letter_list = []
    for letter in (operand_one + operand_two + result):
        if letter not in letter_list:
            letter_list.append(letter)
    assert len(letter_list) <= 10
    assert len(result) <= len(operand_two) + 1 and len(result) <= len(operand_one) + 1
    assert len(result) >= len(operand_two) and len(result) >= len(operand_one)
    while len(letter_list) < 10:
        letter_list.append('_')

    def calculate_number(string, letter_values):
        return sum(
            letter_values.index(letter) * 10 ** power_ten
            for power_ten, letter in enumerate(string[::-1])
        )

    #print(calculate_number("SEND"))
    #assert calculate_number("SEND") == 1230

    def fitness(letter_values):
        first_number = calculate_number(input_data[0], letter_values)
        second_number = calculate_number(input_data[1], letter_values)
        resulting_number = calculate_number(input_data[2], letter_values)

        sum = first_number + second_number
        return abs(sum - resulting_number)

    def create_offspring(parent):
        rand_one = random.randint(0,9)
        rand_two = random.randint(0,9)
        while rand_two == rand_one:
            rand_two = random.randint(0,9)
        offspring = copy.copy(parent)
        offspring[rand_one], offspring[rand_two] = offspring[rand_two], offspring[rand_one]
        return offspring

    def create_new_generation(current_generation):
        return [create_offspring(current_generation) for _ in range(10)]

    def find_fittest_offspring(generation, letter_values):
        current_fittest_index, current_fittest_value = 100, 1000000
        for index, offspring in enumerate(generation):
            if fitness(offspring) < current_fittest_value:
                current_fittest_value = fitness(offspring)
                current_fittest_index = index
        return generation[current_fittest_index]

    #first_generation =
    while True:
        new_generation = create_new_generation(letter_list)
        best_candidate = find_fittest_offspring(new_generation, letter_list)
        letter_list = best_candidate
        if fitness(letter_list) == 0:
            return best_candidate
        else:
            print(f'current best candidate is {best_candidate} with fitness of {fitness(best_candidate)}')

#assert(calculate())
print(solve('SEND', 'MORE', 'MONEY'))





#assert solve('SEND', 'MORE', 'MONEY') == ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

