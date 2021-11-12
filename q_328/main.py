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
    if not ll:
        return []

    arr = [ll.val]
    ll = ll.next
    while ll:
        arr.append(ll.val)
        ll = ll.next
    return arr


class Tests(unittest.TestCase):
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handling the edge case
        if not head or not head.next:
            return head

        # keeps the same memory address of the object
        h_odd = head  # I dont think that we actually need this value
        h_evn = head.next

        # checking to make sure that the memory address is the same
        # print(head is h_odd)
        # print(head.next is h_evn)

        # starting the iteration through the different nodes
        head = head.next.next
        h_odd_node = h_odd
        h_evn_node = h_evn

        # initializing our counter to know if we are on odd or even
        counter = 0
        while head:
            # checking if we are at an even or odd number
            if counter % 2 == 0:
                h_odd_node.next = head
                h_odd_node = h_odd_node.next
                if not head.next:
                    h_evn_node.next = None

            else:
                h_evn_node.next = head
                h_evn_node = h_evn_node.next
                if not head.next:
                    h_odd_node.next = None

            # iterating to the next value
            head = head.next
            counter += 1

        # completing the loop into a single linked list
        h_odd_node.next = h_evn
        return h_odd

    def test1(self):
        input = linkedListFromArray(
            [1, 2, 3, 4, 5]
        )
        resp = self.oddEvenList(input)
        output = [1, 3, 5, 2, 4]
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test2(self):
        input = linkedListFromArray(
            [2, 1, 3, 5, 6, 4, 7]
        )
        resp = self.oddEvenList(input)
        output = [2, 3, 6, 7, 1, 5, 4]
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test3(self):
        input = linkedListFromArray(
            []
        )
        resp = self.oddEvenList(input)
        output = []
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test4(self):
        input = linkedListFromArray(
            [1]
        )
        resp = self.oddEvenList(input)
        output = [1]
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test5(self):
        input = linkedListFromArray(
            [1, 2]
        )
        resp = self.oddEvenList(input)
        output = [1, 2]
        self.assertEqual(arrayFromLinkedList(resp), output)

    def test6(self):
        input = linkedListFromArray(
            [1, 2, 3]
        )
        resp = self.oddEvenList(input)
        output = [1, 3, 2]
        self.assertEqual(arrayFromLinkedList(resp), output)


if __name__ == '__main__':
    unittest.main()
