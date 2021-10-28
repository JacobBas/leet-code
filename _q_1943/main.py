import unittest
from typing import List
from collections import defaultdict


def splitPainting(segments: List[List[int]]) -> List[List[int]]:
    # via this mapping, we can easily know which coordinates should be took into consideration.
    mapping = defaultdict(int)

    # looping through the start end and color to track the values;
    # we are finding the sum/difference of the colors at each of the endpoints
    # to easily track where the colors are mixing
    for s, e, c in segments:
        mapping[s] += c
        mapping[e] -= c

    res = []
    prev, color = None, 0
    for now in sorted(mapping):
        # if color == 0, it means this part isn't painted.
        if prev is not None and color != 0:
            # append to the end of our resp
            res.append([prev, now, color])

        # increment color so that we have the total color of a given segment
        color += mapping[now]
        # store the current value within previous
        prev = now

    return res


class Tests(unittest.TestCase):
    def test0(self):
        input = [[1, 4, 5], [3, 7, 7]]
        output = [[1, 3, 5], [3, 4, 12], [4, 7, 7]]
        self.assertEqual(splitPainting(input), output)

    def test1(self):
        input = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]
        output = [[1, 4, 14], [4, 7, 16]]
        self.assertEqual(splitPainting(input), output)

    def test2(self):
        input = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]
        output = [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]
        self.assertEqual(splitPainting(input), output)

    def test3(self):
        input = [[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]
        output = [[1, 4, 12], [4, 7, 12]]
        self.assertEqual(splitPainting(input), output)


if __name__ == '__main__':
    unittest.main()
