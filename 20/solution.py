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

    def __iter__(self) -> Generator['Node', None, None]:
        cur = self  # type: Optional['Node']
        while cur is not None:
            yield cur
            cur = cur.next

    def __len__(self) -> int:
        return sum(1 for el in self)

    def __next__(self) -> Optional['Node']:
        return self.next


def advance(it: Iterator, n: int) -> None:
    for i in range(n):
        next(it)


def find_intersection_measure(A: Node, B: Node) -> Optional[Node]:
    a_len = len(A)
    b_len = len(B)
    if a_len > b_len:
        advance(iter(A), a_len - b_len)
    else:
        advance(iter(B), b_len - a_len)
    for (a, b) in zip(A, B):
        if a.value == b.value:
            return a
    return None


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        A = Node(3, Node(7, Node(8, Node(10))))
        B = Node(99, Node(1, Node(8, Node(10))))
        inter = find_intersection_measure(A, B)
        assert inter
        self.assertEqual(inter.value, 8)


if __name__ == '__main__':
    unittest.main()
