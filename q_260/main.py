import unittest
from typing import List
from functools import reduce


class Tests(unittest.TestCase):
    def singleNumber(self, nums: List[int]) -> List[int]:
        # initializing the needed varibles
        # xor: exclusive or binary representation
        # a is the first unique value
        # b is the second unique value
        xor, a, b, mask = 0, 0, 0, 1

        for num in nums:
            # this results in a removal of numbers that
            # are repeated since we are using the exclusive
            # or method on the binary representation;
            # since all numbers have 2 occurances other than
            # a and b, the final xor == a^b
            xor ^= num

        # run while xor and mask have no intersection to them by shifting
        # the mask bit over by 1 every iteration:
        # 0b1 -> 0b10 -> 0b100 ...
        while(xor & mask == 0):
            print(mask)
            mask = mask << 1

        for num in nums:
            # if number has at least one intersecting value with mask
            # then we find the exclusive or of a
            if num & mask:
                a ^= num
            else:
                b ^= num

        return [a, b]

    def test1(self):
        input = [1, 2, 1, 3, 2, 5]
        output = [3, 5]
        self.assertEqual(self.singleNumber(input), output)

    def test2(self):
        input = [-1, 0]
        output = [-1, 0]
        self.assertEqual(self.singleNumber(input), output)

    def test3(self):
        input = [0, 1]
        output = [1, 0]
        self.assertEqual(self.singleNumber(input), output)

    def test4(self):
        input = [0, 0, 1, 2]
        output = [1, 2]
        self.assertEqual(self.singleNumber(input), output)

    def test5(self):
        input = [0, 0, 1, 2]
        output = [1, 2]
        self.assertEqual(self.singleNumber(input), output)

    def test6(self):
        input = [2, 1, 2, 3, 4, 1]
        output = [3, 4]
        self.assertEqual(self.singleNumber(input), output)

    def test7(self):
        input = [3, 4, 2, 2, 1, 1]
        output = [3, 4]
        self.assertEqual(self.singleNumber(input), output)

    def test8(self):
        input = [1, 2, 3, 1, 2, 4]
        output = [3, 4]
        self.assertEqual(self.singleNumber(input), output)

    def test9(self):
        input = [1403617094, -490450406, -1756388866, -967931676, 1878401007,
                 1878401007, -74743538, 1403617094, -1756388866, -74743538, -490450406, -1895772685]
        output = [-1895772685, -967931676]
        self.assertEqual(self.singleNumber(input), output)


if __name__ == '__main__':
    unittest.main()
