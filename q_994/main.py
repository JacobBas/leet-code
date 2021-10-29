import unittest
from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    # number of rows
    rows = len(grid)
    if rows == 0:
        return -1

    # number of cols
    cols = len(grid[0])

    # keeping track of the fresh oranges
    fresh_cnt = 0

    # queue with rotten oranges
    rotten = deque()

    # visit each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                # add the coordinates of the rotten orange
                rotten.append((r, c))
            elif grid[r][c] == 1:
                # update the fresh orange count
                fresh_cnt += 1

    # keeping track of the minutes passes
    minutes_passed = 0

    # if there are rotten oranges in the queue and there are still fresh oranges in the grid then we want to keep looping
    while rotten and fresh_cnt > 0:
        # update the number of minutes passed
        # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
        minutes_passed += 1

        for _ in range(len(rotten)):
            x, y = rotten.popleft()

            # visit all of the adjacent cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # calculate the new coordinates
                xx, yy = x + dx, y + dy

                # ignore if we are out of the boundary
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue

                # ignore the cell if it is empty or visted before
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue

                # update the fresh oranges count
                fresh_cnt -= 1

                # mark the current fresh orange as rotten
                grid[xx][yy] = 2

                # add the current rotten to the queue
                rotten.append((xx, yy))

    # returning out the finalized values to the problem
    return minutes_passed if fresh_cnt == 0 else -1


class TestScore(unittest.TestCase):
    def test1(self):
        input = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        output = 4
        self.assertEqual(orangesRotting(input), output)

    def test2(self):
        input = [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]
        output = -1
        self.assertEqual(orangesRotting(input), output)

    def test3(self):
        input = [
            [0, 2]
        ]
        output = 0
        self.assertEqual(orangesRotting(input), output)

    def test4(self):
        input = [
            [0, 0]
        ]
        output = 0
        self.assertEqual(orangesRotting(input), output)

    def test5(self):
        input = [
            [0, 1]
        ]
        output = -1
        self.assertEqual(orangesRotting(input), output)

    def test6(self):
        input = [
            [1, 2]
        ]
        output = 1
        self.assertEqual(orangesRotting(input), output)

    def test7(self):
        input = [
            [2, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        output = 58
        self.assertEqual(orangesRotting(input), output)


if __name__ == '__main__':
    unittest.main()
