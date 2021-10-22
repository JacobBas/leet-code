import unittest
from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    """
    time complexity  = O(n)
    space complexity = constant
    """
    n = len(mat)
    sum = 0
    for i in range(n):
        if i != len(mat) - i - 1:
            sum += mat[i][n - i - 1]
        sum += mat[i][i]
    return sum


class Tests(unittest.TestCase):
    def test1(self):
        input = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        output = 25
        self.assertEqual(diagonalSum(input), output)

    def test2(self):
        input = [[1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]]
        output = 8
        self.assertEqual(diagonalSum(input), output)

    def test3(self):
        input = [[5]]
        output = 5
        self.assertEqual(diagonalSum(input), output)


if __name__ == '__main__':
    unittest.main()
