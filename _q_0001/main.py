import unittest
from typing import List


class Tests(unittest.TestCase):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value in numsDict:
                return [numsDict[value], i]
            else:
                numsDict[nums[i]] = i

    def test1(self):
        input = [[2, 7, 11, 15], 9]
        output = [0, 1]
        self.assertEqual(self.twoSum(input[0], input[1]), output)

    def test2(self):
        input = [[3, 2, 4], 6]
        output = [1, 2]
        self.assertEqual(self.twoSum(input[0], input[1]), output)

    def test3(self):
        input = [[3, 3], 6]
        output = [0, 1]
        self.assertEqual(self.twoSum(input[0], input[1]), output)


if __name__ == '__main__':
    unittest.main()
