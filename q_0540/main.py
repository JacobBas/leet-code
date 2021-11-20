import unittest
from typing import List


class Tests(unittest.TestCase):
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # we need to check matching index values
        s = 0
        e = len(nums) - 1
        m = e // 2

        # handling the edge cases
        if e == 0:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[e - 1] != nums[e]:
            return nums[e]

        # the even index must match with the value in front
        # the odd numbers must match with the value in the back
        # if this is not true then we are offset by one value
        # or the value that there is only one occurance of
        while s <= e:
            if m % 2 == 0:
                # if the offset is still correct then we move to the right
                if nums[m] == nums[m + 1]:
                    s = m
                    m = (m + e) // 2

                # if the offest is incorrect then we move to the left
                elif nums[m] == nums[m - 1]:
                    e = m
                    m = (m + s) // 2

                else:
                    return nums[m]

            else:
                # if the offset is still correct then we move to the right
                if nums[m] == nums[m - 1]:
                    s = m
                    m = (m + e) // 2

                # if the offest is incorrect then we move to the left
                elif nums[m] == nums[m + 1]:
                    e = m
                    m = (m + s) // 2

                else:
                    return nums[m]

    def test1(self):
        input = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        output = 2
        self.assertEqual(self.singleNonDuplicate(input), output)

    def test2(self):
        input = [3, 3, 7, 7, 10, 11, 11]
        output = 10
        self.assertEqual(self.singleNonDuplicate(input), output)

    def test3(self):
        input = [1]
        output = 1
        self.assertEqual(self.singleNonDuplicate(input), output)

    def test4(self):
        input = [2, 1, 1]
        output = 2
        self.assertEqual(self.singleNonDuplicate(input), output)

    def test5(self):
        input = [1, 1, 2]
        output = 2
        self.assertEqual(self.singleNonDuplicate(input), output)


if __name__ == "__main__":
    unittest.main()
