import unittest


def truncateSentence(s: str, k: int) -> str:
    end, i = 0, 0
    while i < k:
        end = s.find(" ", end) + 1
        i += 1
    return s[:end - 1] if end != 0 else s


class Tests(unittest.TestCase):
    def test1(self):
        input_s = "Hello how are you Contestant"
        input_k = 4
        output = "Hello how are you"
        self.assertEqual(
            truncateSentence(input_s, input_k),
            output,
        )

    def test2(self):
        input_s = "What is the solution to this problem"
        input_k = 4
        output = "What is the solution"
        self.assertEqual(
            truncateSentence(input_s, input_k),
            output,
        )

    def test3(self):
        input_s = "chopper is not a tanuki"
        input_k = 5
        output = "chopper is not a tanuki"
        self.assertEqual(
            truncateSentence(input_s, input_k),
            output,
        )


if __name__ == "__main__":
    unittest.main()
