
class Rope:

    def __init__(self, entries):
        self.contents = [entries] if isinstance(entries, str) else entries

    def __str__(self):
        return "".join(str(object) for object in self.contents)

    def __len__(self):
        return sum(len(object) for object in self.contents)

    def _index_of(self, character):
        index_count = 0
        for object in self.contents:
            if isinstance(object, str):
                for letter in object:
                    if letter == character:
                        return True, index_count
                    else:
                        index_count += 1
            else:
                x, y = object._index_of(character)
                index_count += y
                if x:
                    return True, index_count

        return False, index_count

    def index_of(self, character):
        x, y = self._index_of(character)
        if x:
            return y
        else:
            return None

    @classmethod
    def concatenate(cls, rope_1, rope_2):
        return Rope([rope_1, rope_2])


x = Rope("hello world")
y = Rope.concatenate(Rope("helllllo"), Rope("woooorld"))
print(str(x))
print(str(y))
print(str(Rope.concatenate(x, y)))
print(len(Rope.concatenate(x, y)))
print(y.index_of("d"))
print(str(y).index("d"))
