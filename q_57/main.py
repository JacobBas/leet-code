import unittest
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    time complexity  = O(n)
    space complexity = constant
    """

    if intervals:
        if newInterval[1] < intervals[0][0]:
            # inserting at the front of the max of newInterval
            # is less that the min of the current
            intervals.insert(0, newInterval)

        else:
            lower_i = len(intervals)  # the index that fits the lower interval
            upper_i = 0               # the index that fits the upper interval

            # checking where to insert the value
            for i in range(len(intervals)):
                if newInterval[0] <= intervals[i][1]:
                    lower_i = min(i, lower_i)
                if newInterval[1] >= intervals[i][0]:
                    upper_i = i

            if lower_i == len(intervals):
                # appending the newInterval to the end
                intervals.append(newInterval)

            else:
                # assigning the new interval
                newInterval[0] = min(intervals[lower_i][0], newInterval[0])
                newInterval[1] = max(intervals[upper_i][1], newInterval[1])

                # removing old indecies
                for i in reversed(range(lower_i, upper_i+1)):
                    intervals.pop(i)

                # inserting in the new index
                intervals.insert(lower_i, newInterval)

    else:
        # edge case where we append into an empty array
        intervals.append(newInterval)

    return intervals


class TestAnswers(unittest.TestCase):
    def test1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        output = [[1, 5], [6, 9]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        output = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test3(self):
        intervals = []
        newInterval = [5, 7]
        output = [[5, 7]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test4(self):
        intervals = [[1, 5]]
        newInterval = [2, 3]
        output = [[1, 5]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test5(self):
        intervals = [[1, 5]]
        newInterval = [2, 7]
        output = [[1, 7]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test6(self):
        intervals = [[1, 5]]
        newInterval = [6, 8]
        output = [[1, 5], [6, 8]]
        self.assertEqual(insert(intervals, newInterval), output)

    def test7(self):
        intervals = [[6, 8]]
        newInterval = [1, 5]
        output = [[1, 5], [6, 8]]
        self.assertEqual(insert(intervals, newInterval), output)


if __name__ == '__main__':
    unittest.main()
