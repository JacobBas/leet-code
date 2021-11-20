import unittest
from typing import List
from functools import reduce


class Tests(unittest.TestCase):
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        for i in range(1, len(nums) + 1):
        	sub_total = sum(nums[:i])
        	if sub_total > total - sub_total:
        		return nums[:i]

    def test1(self):
        input = [4, 3, 10, 9, 8]
        output = [10, 9]
        self.assertEqual(
            self.minSubsequence(input),
            output,
        )

    def test2(self):
        input = [4, 4, 7, 6, 7]
        output = [7, 7, 6]
        self.assertEqual(
            self.minSubsequence(input),
            output,
        )

    def test3(self):
        input = [6]
        output = [6]
        self.assertEqual(
            self.minSubsequence(input),
            output,
        )


if __name__ == "__main__":
    unittest.main()
