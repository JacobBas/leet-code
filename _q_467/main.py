import unittest
from collections import defaultdict
import string

s = string.ascii_lowercase


def findSub(p: str) -> int:
    letter_dict = defaultdict(int)
    streak = 0
    for i in range(len(p)):
        streak = letter_dict[l]
        print(streak)


class Tests(unittest.TestCase):
    def test1(self):
        input = "a"
        output = 1
        self.assertEqual(findSub(input), output)

    def test2(self):
        input = "cac"
        output = 2
        self.assertEqual(findSub(input), output)

    def test3(self):
        input = "zab"
        output = 6
        self.assertEqual(findSub(input), output)


if __name__ == '__main__':
    unittest.main()
