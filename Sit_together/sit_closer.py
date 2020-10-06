"""
There are M people sitting in a row of N seats, where M < N. 
Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1],
where 0 represents an empty seat and 1 represents a person. 
In this case, one solution would be to place the person on the right in the fourth seat. 
We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
"""
#testcases:
input0 = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
input1 = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
input2 = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
input3 = [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
input4 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]

def process(input):
    M = 0
    starting_seats = []
    for index, x in enumerate(input):
        if x == 1:
            M += 1
            starting_seats.append(index)
    return M, starting_seats

#N = len(input)
#M, starting_seats = process(input

def find_median_seat(M, starting_seats):
    if M % 2 == 1:
        return starting_seats[ (M-1) // 2 ]
    else:
        return (starting_seats[ M // 2 ] + starting_seats[ M // 2 - 1 ]) // 2

def determine_final_seats(M, median_seat):
    first_seat = median_seat + (1 - M) // 2
    last_seat = median_seat + (M - 1) // 2
    seats = range(first_seat, last_seat + 1)
    return seats

def determine_cost(final_seats, starting_seats):
    cost = 0
    for index, value in enumerate(final_seats):
        cost += abs(value - starting_seats[index])
    return cost


#determine_final_seats(find_median_seat(process(input))) <-- need to unpack tuples in function arguments
def whole_thing_together(input):
    M, starting_seats = process(input)
    median_seat = find_median_seat(M,starting_seats)
    final_seats = determine_final_seats(M, median_seat)
    cost = determine_cost(final_seats, starting_seats)
    print(cost)

whole_thing_together(input0)
whole_thing_together(input1)
whole_thing_together(input2)
whole_thing_together(input3)
whole_thing_together(input4)

