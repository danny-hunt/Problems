"""Create a data structure that performs all the following operations in O(1) time:

* plus: Add a key with value 1. If the key already exists, increment its value by one.
* minus: Decrement the value of a key. If the key's value is currently 1, remove it.
* get_max: Return a key with the highest value.
* get_min: Return a key with the lowest value.
"""

class Structure(dict):
    def __init__(self):
        self.size_list = [set()]
        self.size_list_largest_index = 0
        self.smallest_value = 0
        self.greatest_value = 0

    def plus(self, key):
        key_string = str(key)
        if key_string in self:
            self[key_string] += 1
        else:
            self[key_string] = 1
            self.size_dict[str(1)] = self[key_string]

    def minus(self,key):
        key_string = str(key)
        self[key_string] -= 1
        new_index = self[key_string]
        if new_index > 1:
            self.size_dict[str(new_index)].append(key_string)
            self.size_dict[str(new_index + 1)].remove(key)

        else:
            self.pop(key_string)


    def get_max(self):
        return self.greatest_value

    def get_min(self):
        return self.smallest_value


example = Structure()
example.plus('help')
example.plus('help')
example.plus('5')
example.plus('5')
example.minus('5')
example.minus('help')
example.minus('5')
assert example.get_max() == 'help'
assert example.get_min() == 'help'