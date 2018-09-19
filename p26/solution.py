"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k,
remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""
import unittest
from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None  # type: Optional[Node]


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, n: Node) -> None:
        if not self.head:
            self.head = n
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = n

    def to_list(self) -> List[int]:
        l = []
        last = self.head
        while last.next:
            l.append(last.value)
            last = last.next
        l.append(last.value)
        return l

    def remove_kth_last(self, k) -> None:
        main_ptr, head_ptr = self.head, self.head
        for _ in range(k):
            head_ptr = head_ptr.next
        while head_ptr.next:
            head_ptr = head_ptr.next
            main_ptr = main_ptr.next
        main_ptr.next = main_ptr.next.next


class TestSolution(unittest.TestCase):
    def test_create_linked_list(self) -> None:
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        self.assertEqual(ll.to_list(), [1, 2])

    def test_k1(self) -> None:
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.remove_kth_last(1)
        self.assertEqual(ll.to_list(), [1, 2])

    def test_k2(self) -> None:
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.remove_kth_last(2)
        self.assertEqual(ll.to_list(), [1, 3])

    def test_k3(self) -> None:
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.append(Node(4))
        ll.remove_kth_last(3)
        self.assertEqual(ll.to_list(), [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
