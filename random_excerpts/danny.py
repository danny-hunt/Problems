import unittest

words = ["anime",
         "meme",
         "tiktoks",
         "roasts",
         "Danny DeVito"
         ]

hot_words = [ [x, len(x)] for x in words]


def prevent_distractions(string):
    distractions = ["anime", "meme", "tiktoks", "roasts", "Danny DeVito"]
    for index in range(len(string)):
        for word in distractions:
            if string[index: (index + len(word))] == word:
                return "NO!"
    return "Safe watching!"


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("NO!", prevent_distractions("tiktoks that butter my eggroll"))

    def test_2(self):
        self.assertEqual("NO!", prevent_distractions("Hot pictures of Danny DeVito"))

    def test_3(self):
        self.assertEqual("NO!", prevent_distractions("top 10 insert random yt celebrity roasts"))

    def test_4(self):
        self.assertEqual("NO!", prevent_distractions("best anime food ever!"))

    def test_5(self):
        self.assertEqual("Safe watching!", prevent_distractions("How to Be a Productive Member of Society"))


if __name__ == "__main__":
    unittest.main()
