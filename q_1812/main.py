import unittest

class Tests(unittest.TestCase):
    letter_hash = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
    }

    def squareIsWhite(self, coordinates: str) -> bool:
        # pulling out the letter and number seperatly
        letter = self.letter_hash[coordinates[0]]
        number = int(coordinates[1])

        # if they are both odd or even then the square is black
        if (letter % 2) == (number % 2):
            return False
        else:
            return True

    def test1(self):
        input = "a1"
        output = False
        self.assertEqual(
            self.squareIsWhite(input), 
            output,
        )

    def test2(self):
        input = "h3"
        output = True
        self.assertEqual(
            self.squareIsWhite(input), 
            output,
        )

    def test3(self):
        input = "c7"
        output = False
        self.assertEqual(
            self.squareIsWhite(input), 
            output,
        )

if __name__ == '__main__':
    unittest.main()
