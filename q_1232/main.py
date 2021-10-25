import unittest
import math
from typing import List 


def checkStraightLine(coordinates: List[List[int]]) -> bool:
	"""
	time complexity = O(n)
	space complexity = constant
	"""
	# initializing our comparison slope value
	num = coordinates[1][1] - coordinates[0][1]
	den = coordinates[1][0] - coordinates[0][0]
	if den == 0:
		slope = math.inf
	else:
		slope = num / den

	# checking the initial slope against all other slopes
	slope_check = 0
	for i in range(2, len(coordinates)):
		num = coordinates[i][1] - coordinates[i-1][1]
		den = coordinates[i][0] - coordinates[i-1][0]
		if den == 0:
			slope_check = math.inf
		else:
			slope_check = num/den

		if slope_check != slope:
			return False

	return True


class Tests(unittest.TestCase):
	def test1(self):
		input = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
		output = True
		self.assertEqual(checkStraightLine(input), output)

	def test2(self):
		input = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
		output = False
		self.assertEqual(checkStraightLine(input), output)

	def test3(self):
		input = [[0,0],[0,1],[0,-1]]
		output = True
		self.assertEqual(checkStraightLine(input), output)

	def test3(self):
		input = [[0,0],[1,0],[-1,0]]
		output = True
		self.assertEqual(checkStraightLine(input), output)

	def test4(self):
		input = [[0,0],[0,5],[5,5],[5,0]]
		output = False
		self.assertEqual(checkStraightLine(input), output)


if __name__ == "__main__":
	unittest.main()
