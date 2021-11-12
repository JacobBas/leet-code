import unittest


def sqrt(x: int) -> int:
    """
    time complexity =  O(log(n))
    space complexity = constant
    """
    # handling the edge case
    if x < 2:
        return x
    # initializing the left and right values
    l, r = 0, x
    while l <= r:
        # midpoint of the left and right sides
        mid = (l+r)//2
        # if x is inbetween the mid values
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        # if x is less than the square of the mid
        elif x < mid * mid:
            r = mid
        # if x is greater than than mid squared
        else:
            l = mid


class Tests(unittest.TestCase):
    def test1(self):
        input = 4
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test2(self):
        input = 8
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test3(self):
        input = 15
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test4(self):
        input = 45
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test5(self):
        input = 1238
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test6(self):
        input = 1230322
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test7(self):
        input = 0
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)

    def test8(self):
        input = 1
        output = sqrt(input)
        self.assertEqual(sqrt(input), output)


if __name__ == '__main__':
    unittest.main()
