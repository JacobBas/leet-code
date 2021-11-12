import unittest
from typing import List
import math
from collections import defaultdict


def findShortestSubArray(nums: List[int]) -> int:
    # initializing the dictionary of possible values
    i_dict = defaultdict(list)

    # populating the dictionary of indecies
    for i in range(len(nums)):
        i_dict[nums[i]] += [i]

    # initializing the degree and length varibles
    degree, length = 0, math.inf

    # looping through the values in the dictionary
    for i in i_dict.values():
        # length of the current sub array
        n = 1 + i[-1] - i[0]

        # if the degree is higher than we set length
        if len(i) > degree:
            degree = len(i)
            length = n

        # if the degree is equal then we check if shorter and set
        elif len(i) == degree:
            if n < length:
                length = n

    return length


class Tests(unittest.TestCase):
    def test1(self):
        input = [1, 2, 2, 3, 1]
        output = 2
        self.assertEqual(findShortestSubArray(input), output)

    def test2(self):
        input = [1, 2, 2, 3, 1, 4, 2]
        output = 6
        self.assertEqual(findShortestSubArray(input), output)

    def test3(self):
        input = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
        output = 9
        self.assertEqual(findShortestSubArray(input), output)


if __name__ == '__main__':
    unittest.main()
