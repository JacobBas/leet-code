import unittest
from typing import List
from collections import deque


def solveOrig(board: List[List[str]]) -> None:
    m = len(board)
    n = len(board[0])
    q = deque()
    # checking the outside of the board
    for i in range(1, n - 1):
        if board[0][i] == "O":
            q.append([0, i])

    for i in range(1, n - 1):
        if board[m-1][i] == "O":
            q.append([m-1, i])

    for i in range(m):
        if board[i][0] == "O":
            q.append([i, 0])

    for i in range(m):
        if board[i][n-1] == "O":
            q.append([i, n-1])

    if len(q) == 0:
        for i in range(m):
            for j in range(n):
                board[i][j] = "X"
        return

    # checking if the neighboring items are "O"
    f = []
    while len(q) > 0:
        item = q.pop()
        # checking top
        if item[1] - 1 > 0:
            if board[item[0]][item[1] - 1] == "O" and [item[0], item[1] - 1] not in f:
                q.append([item[0], item[1] - 1])

        # checking right
        if item[0] + 1 < m:
            if board[item[0] + 1][item[1]] == "O" and [item[0] + 1, item[1]] not in f:
                q.append([item[0] + 1, item[1]])

        # checking bottom
        if item[1] + 1 < n:
            if board[item[0]][item[1] + 1] == "O" and [item[0], item[1] + 1] not in f:
                q.append([item[0], item[1] + 1])

        # checking left
        if item[0] - 1 > 0:
            if board[item[0] - 1][item[1]] == "O" and [item[0] - 1, item[1]] not in f:
                q.append([item[0] - 1, item[1]])

        f.append(item)

    # updating the board to be correct
    for i in range(m):
        for j in range(n):
            if [i, j] not in f:
                board[i][j] = "X"


def solve(board: List[List[str]]) -> None:
    # getting the dimensions of the board
    m = len(board)
    n = len(board[0])

    # if the board is 2x2 or less then we just return the board
    if m <= 2 or n <= 2:
        return

    # defining a function of the border of the square
    def markBorder(i, j):
        # if i is in the correct range and j is in the correct range and
        # the cell is equal to 'O' then we go recursivley through the
        # neighboring elements to see if they are attached to the border
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'B'
            markBorder(i + 1, j)
            markBorder(i - 1, j)
            markBorder(i, j + 1)
            markBorder(i, j - 1)

    # going through the left and right borders
    for i in range(m):
        markBorder(i, 0)
        markBorder(i, n - 1)

    # going through the top and the bottom borders
    for j in range(n):
        markBorder(0, j)
        markBorder(m - 1, j)

    # looping through all elements of the board:
    # if 'X' then ignore
    # if 'O' then change to 'X'
    # if 'B' then change to 'O'
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            if c != 'X':
                board[i][j] = 'X' if c == 'O' else 'O'


class Tests(unittest.TestCase):
    """
    Solving the data in place so the input should equal the output
    once the function has been run
    """

    def test1(self):
        input = [["X", "X", "X", "X"],
                 ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"],
                 ["X", "O", "X", "X"]]
        output = [["X", "X", "X", "X"],
                  ["X", "X", "X", "X"],
                  ["X", "X", "X", "X"],
                  ["X", "O", "X", "X"]]
        solve(input)
        self.assertEqual(input, output)

    def test2(self):
        input = [["X"]]
        output = [["X"]]
        solve(input)
        self.assertEqual(input, output)

    def test3(self):
        input = [["X", "X", "X"],
                 ["X", "O", "X"],
                 ["X", "X", "X"]]
        output = [["X", "X", "X"],
                  ["X", "X", "X"],
                  ["X", "X", "X"]]
        solve(input)
        self.assertEqual(input, output)

    def test4(self):
        input = [["X", "O", "X", "O", "X", "O"],
                 ["O", "X", "O", "X", "O", "X"],
                 ["X", "O", "X", "O", "X", "O"],
                 ["O", "X", "O", "X", "O", "X"]]
        output = [["X", "O", "X", "O", "X", "O"],
                  ["O", "X", "X", "X", "X", "X"],
                  ["X", "X", "X", "X", "X", "O"],
                  ["O", "X", "O", "X", "O", "X"]]
        solve(input)
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
