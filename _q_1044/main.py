import unittest


def longestDupSubstring(s: str) -> str:
    # todo need to look into rabin-karps algorithm in CLRS
    pass


class TestCase(unittest.TestCase):
    def test1(self):
        input = "banana"
        output = "ana"
        self.assertEqual(longestDupSubstring(input), output)

    def test2(self):
        input = "abcd"
        output = ""
        self.assertEqual(longestDupSubstring(input), output)


if __name__ == '__main__':
    unittest.main()
