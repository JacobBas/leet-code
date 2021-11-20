import unittest


class Tests(unittest.TestCase):
    def isPalendrome(self, x: int) -> bool:
        # handling the edge cases
        if x < 0:
            return False

        if x < 10:
            return True

        # checking the equality of mirrored values
        x = str(x)
        m = len(x) // 2
        for i in range(m):
            if x[i] != x[-1 - i]:
                return False

        return True

    def test1(self):
        input = 121
        output = True
        self.assertEqual(
            self.isPalendrome(input),
            output,
        )

    def test2(self):
        input = -121
        output = False
        self.assertEqual(
            self.isPalendrome(input),
            output,
        )

    def test3(self):
        input = 10
        output = False
        self.assertEqual(
            self.isPalendrome(input),
            output,
        )

    def test4(self):
        input = -101
        output = False
        self.assertEqual(
            self.isPalendrome(input),
            output,
        )


if __name__ == '__main__':
    unittest.main()
