import unittest
import functools

class Problem(unittest.TestCase):
    def factorial(self, n: int) -> int:
        return functools.reduce(lambda x, y: x*y, range(1, n + 1), 1)

    def uniquePaths1(self, m: int, n: int) -> int:
        return self.factorial(m + n - 2) // (self.factorial(m - 1) * self.factorial(n - 1))

    def uniquePaths(self, m: int, n: int) -> int:
        # initializing the numbers
        resp = 1

        # looping through the values
        for i in range(1, m + n - 1):
            resp *= i
            if i < n:
                resp /= i
            else:
                resp /= i - n + 1

        # returning out the final number of combos
        return resp

    def test1(self):
        input = {"m": 3, "n": 7}
        output = 28
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )

    def test2(self):
        input = {"m": 3, "n": 2}
        output = 3
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )

    def test3(self):
        input = {"m": 7, "n": 3}
        output = 28
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )

    def test4(self):
        input = {"m": 3, "n": 3}
        output = 6
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )

    def test5(self):
        input = {"m": 1, "n": 2}
        output = 1
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )

    def test5(self):
        input = {"m": 4, "n": 4}
        output = 20
        self.assertEqual(
            self.uniquePaths(input["m"], input["n"]),
            output
        )


if __name__ == '__main__':
    unittest.main()
