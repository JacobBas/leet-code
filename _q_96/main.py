import unittest
from typing import List


class Tests(unittest.TestCase):
    def treeCount(self, count: List[int], n: int):
        if n <= 0:
            return

        count[0] += 1
        for i in range(n):
            print("left:", i, "right:", n-1-i)
            # left side
            self.treeCount(count, i)
            # right side
            self.treeCount(count, n-1-i)

    def numTrees(self, n: int) -> int:
        count = [0]
        self.treeCount(count, n)
        return count[0]

    def test1(self):
        input = 1
        output = 1
        self.assertEqual(self.numTrees(input), output)

    def test2(self):
        input = 2
        output = 2
        self.assertEqual(self.numTrees(input), output)

    # def test3(self):
    #     input = 3
    #     output = 5
    #     self.assertEqual(self.numTrees(input), output)

    # def test4(self):
    #     input = 4
    #     output = 14
    #     self.assertEqual(self.numTrees(input), output)


if __name__ == '__main__':
    unittest.main()
