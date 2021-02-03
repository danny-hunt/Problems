import time
import itertools

board = [[0] * 8 for _ in range(8)]
squares = itertools.product(range(8), repeat=2)

possible_placements = itertools.combinations(squares, 7)

square_dict = {}


def can_see_from(square):
    if square in square_dict:
        return square_dict[square]
    else:
        attacked_squares = set()
        for x in range(8):
            if x != square[0]:
                attacked_squares.add((x, square[1]))
        for y in range(8):
            if y != square[1]:
                attacked_squares.add((square[0], y))
        for x in range(1,3):
            for y in range(1,3):
                attacked_squares.add((square[0] + x, square[1] + y))
                attacked_squares.add((square[0] - x, square[1] + y))
                attacked_squares.add((square[0] + x, square[1] - y))
                attacked_squares.add((square[0] - x, square[1] - y))
        for z in range(1,8):
            attacked_squares.add((square[0] + z, square[1] + z))
            attacked_squares.add((square[0] - z, square[1] - z))
            attacked_squares.add((square[0] + z, square[1] - z))
            attacked_squares.add((square[0] - z, square[1] + z))

        output_set = set()
        for square in attacked_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                output_set.add(square)
        square_dict[square] = output_set
        #print(output_set)
        #print(len(output_set))
        return square_dict[square]


test_set = set()
test_placement = ((0, 0), (4,1), (1, 3), (2, 6), (5, 4), (6, 7))
for fairy in test_placement:
    test_set = test_set.union(can_see_from(fairy))
    print(len(test_set))
print(test_set)
for fairy in test_placement:
    if fairy in test_set:
        print(fairy)
if any(fairy in test_set for fairy in test_placement):
    print("help")
else:
    print("test set is successful")

print(list(possible_placements))
counter = 0
start_time = time.time()
for placement in possible_placements:
    if counter % 1000000 == 0:
        print(f" {counter // 1000000} million many done! in {time.time() - start_time}s")

    counter += 1
    danger_set = set()
    for fairy in placement:
        danger_set = danger_set.union(can_see_from(fairy))
    #print(f" placement is : {placement}")
    #print(f" danger_set is {danger_set}")
    if any(fairy in danger_set for fairy in placement):
        pass
    else:
        print(f"successful placement is {placement}")


