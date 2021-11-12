import unittest
from typing import List
import math


def permRec(final: List[List[int]], curr: List[int], opt: List[int]):
    # handling the end node of the recursive function
    if len(opt) == 0:
        final.append(curr)
        return final

    # looping through the permutations of the unique values
    for i in range(len(opt)):
        # add the new value onto our permutation
        new_curr = curr + [opt[i]]
        # copy the options list and remove the option that has just been used
        new_opt = opt.copy()
        new_opt.pop(i)
        # start a new recursive iteration
        permRec(final, new_curr, new_opt)


def permuteUnique(nums: List[int]) -> List[List[int]]:
    # initialize return list
    final = []
    # start our recursive function for permutations
    permRec(final, [], nums)
    # return out our values
    return final


class Tests(unittest.TestCase):
    def test1(self):
        input = [1, 2, 3]
        output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], 
                  [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(permuteUnique(input), output)

    def test2(self):
        input = [0, 1]
        output = [[0, 1], [1, 0]]
        self.assertEqual(permuteUnique(input), output)

    def test3(self):
        input = [1]
        output = [[1]]
        self.assertEqual(permuteUnique(input), output)


if __name__ == "__main__":
    unittest.main()
