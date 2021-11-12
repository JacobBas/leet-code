import unittest
from typing import List


def validTicTacToe(board: List[str]) -> bool:
    # checking the initial character combinations
    char_hash = {" ": 0, "X": 0, "O": 0}
    for i in range(3):
        for j in range(3):
            char_hash[board[i][j]] += 1

    if char_hash["O"] > char_hash["X"]:
        return False
    if char_hash["X"] - char_hash["O"] not in [1, 0]:
        return False

    # checking the winning states on the board
    win_track = {" ": False, "X": False, "O": False}
    # tracking the row wins
    for i in range(3):
        win_track[board[i][0]] = (
            board[i][0] == board[i][1] == board[i][2]) or win_track[board[i][0]]

    # track the column wins
    for i in range(3):
        win_track[board[0][i]] = (
            board[0][i] == board[1][i] == board[2][i]) or win_track[board[0][i]]

    # track the diagonal wins
    win_track[board[1][1]] = (board[0][0] == board[1]
                              [1] == board[2][2]) or win_track[board[1][1]]
    win_track[board[1][1]] = (board[0][2] == board[1]
                              [1] == board[2][0]) or win_track[board[1][1]]

    if win_track["X"] and win_track["O"]:
        return False
    if win_track["X"] and char_hash["X"] - char_hash["O"] != 1:
        return False
    if win_track["O"] and char_hash["X"] - char_hash["O"] != 0:
        return False

    return True


class Tests(unittest.TestCase):
    def test1(self):
        """
        false since X must always go before O
        """
        input = ["O  ", "   ", "   "]
        output = False
        self.assertEqual(validTicTacToe(input), output)

    def test2(self):
        """
        false since the number of X's can be at most 1 greater than the
        number or O's
        """
        input = ["XOX", " X ", "   "]
        output = False
        self.assertEqual(validTicTacToe(input), output)

    def test3(self):
        """
        false since there can only be one winning combination
        """
        input = ["XXX", "   ", "OOO"]
        output = False
        self.assertEqual(validTicTacToe(input), output)

    def test4(self):
        """
        true because valid board
        """
        input = ["XOX", "O O", "XOX"]
        output = True
        self.assertEqual(validTicTacToe(input), output)

    def test5(self):
        """
        false because X won so O must have one less character
        """
        input = ["XXX", "XOO", "OO "]
        output = False
        self.assertEqual(validTicTacToe(input), output)


if __name__ == "__main__":
    unittest.main()
