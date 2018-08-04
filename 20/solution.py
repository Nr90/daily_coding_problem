"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
import unittest
from typing import Generator, Optional, Iterator


class Node:
    def __init__(self, value: int, next: 'Node'=None) -> None:
        self.value = value
        self.next = next


def find_intersection(A: Node, B: Node) -> Optional[Node]:
    if A is None or B is None:
        return None
    
    a, b = A, B
    while a is not b:
        if a == None:
            a = B
        else:
            a = a.next
        if b == None:
            b = A
        else:
            b = b.next
    return a


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        shared = Node(8, Node(10))
        A = Node(3, Node(7, shared))
        B = Node(99, Node(1, shared))
        inter = find_intersection(A, B)
        assert inter
        self.assertEqual(inter, shared)

    def test_unequal_length(self) -> None:
        shared = Node(8, Node(10))
        A = Node(7, shared)
        B = Node(99, Node(1, shared))
        inter = find_intersection(A, B)
        assert inter
        self.assertEqual(inter, shared)


if __name__ == '__main__':
    unittest.main()
