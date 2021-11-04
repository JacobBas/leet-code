import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverseLeftSum(node):
    if node:
        val = 0
        if node.left and not node.left.left and not node.left.right:
            val = node.left.val
        return val + traverseLeftSum(node.left) + traverseLeftSum(node.right)

    else:
        return 0


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    return traverseLeftSum(root)


class Tests(unittest.TestCase):
    def test1(self):
        input = [3, 9, 20, None, None, 15, 7]
        output = 24
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        self.assertEqual(sumOfLeftLeaves(root), output)

    def test2(self):
        input = [1]
        output = 0
        root = TreeNode(1)
        self.assertEqual(sumOfLeftLeaves(root), output)

    def test3(self):
        input = [1, 2, 3, 4, 5]
        output = 4
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(sumOfLeftLeaves(root), output)


if __name__ == '__main__':
    unittest.main()
