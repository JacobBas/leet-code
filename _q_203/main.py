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
        head_iter = head
        while head_iter:
            print(head_iter.val)
            head_iter = head_iter.next
        return head

    def test1(self):
        head = linkedListFromArray([1, 2, 6, 3, 4, 5, 6])
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


if __name__ == '__main__':
    unittest.main()
