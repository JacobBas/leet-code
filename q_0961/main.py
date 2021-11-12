import unittest
from collections import defaultdict
from typing import List


def repeatedNTimes(nums: List[int]):
    d = defaultdict(int)
    for i in nums:
        d[i] += 1
        if d[i] >= 2:
            return i


class Tests(unittest.TestCase):
    def test1(self):
        input: List = [1, 2, 3, 3]
        output: int = 3
        self.assertEqual(repeatedNTimes(input), output)

    def test2(self):
        input: List = [2, 1, 2, 5, 3, 2]
        output: int = 2
        self.assertEqual(repeatedNTimes(input), output)

    def test3(self):
        input: List = [5, 1, 5, 2, 5, 3, 5, 4]
        output: int = 5
        self.assertEqual(repeatedNTimes(input), output)


if __name__ == '__main__':
    unittest.main()
