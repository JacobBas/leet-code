import unittest
from typing import List


class Tests(unittest.TestCase):
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = temp

    def test1(self):
        input = ["h", "e", "l", "l", "o"]
        output = ["o", "l", "l", "e", "h"]
        self.reverseString(input)
        self.assertEqual(
            input,
            output,
        )

    def test2(self):
        input = ["H", "a", "n", "n", "a", "h"]
        output = ["h", "a", "n", "n", "a", "H"]
        self.reverseString(input)
        self.assertEqual(
            input,
            output,
        )


if __name__ == '__main__':
    unittest.main()
