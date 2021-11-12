import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListFromArray(arr: List[int]) -> Optional[ListNode]:
    """
    converts an array of integers into a linked list

    Args:
        arr (List): an array of integer values

    Returns:
        Optional[ListNode]: a linked list of integers
    """
    if not arr:
        return None

    root = ListNode(arr[-1])
    for n in reversed(arr[:len(arr) - 1]):
        root = ListNode(n, root)
    return root


def arrayFromLinkedList(ll: Optional[ListNode]) -> str:
    """
    returns the string represetation of a linked list

    Args:
        ll (Optional[ListNode]): a linked list object

    Returns:
        str: string representation of a linked list
    """
    arr = []
    while ll:
        arr.append(ll.val)
        ll = ll.next
    return arr


class Tests(unittest.TestCase):
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        time complexity: O(n) since we are only checking each object once
        space complexity: constant space complexity
        """

        # handling the edge case of the first n values in the linked list
        # being equal to val. In this case we want to keep shifting the
        # linked list over until we get to a point where the linked list
        # starts with a number that is not equal to the val.
        while head and head.val == val:
            head = head.next

        # we finish off be removing values that show up in the middle
        # of the linked list.
        head_iter = head
        while head_iter:
            # handling the case where we have consecutive values
            # showing up within the linked list
            while head_iter.next and head_iter.next.val == val:
                head_iter.next = head_iter.next.next

            # iterating to the next value within the linked list
            head_iter = head_iter.next

        # returning the final list
        return head

    def test1(self):
        head = linkedListFromArray([1, 2, 6, 6, 3, 4, 5, 6])
        val = 6
        resp = self.removeElements(head, val)
        output = [1, 2, 3, 4, 5]
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test2(self):
        head = linkedListFromArray([])
        val = 1
        resp = self.removeElements(head, val)
        output = []
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test3(self):
        head = linkedListFromArray([7, 7, 7, 7])
        val = 7
        resp = self.removeElements(head, val)
        output = []
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test4(self):
        head = linkedListFromArray([1, 7, 7, 7])
        val = 7
        resp = self.removeElements(head, val)
        output = [1]
        self.assertEqual(arrayFromLinkedList(resp), output)


if __name__ == '__main__':
    unittest.main()
