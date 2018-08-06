"""
This problem was asked by Airbnb.

Given a list of integers,
write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
import unittest
from typing import List


def loop(l: List[int]) -> int:
    incl = 0
    excl = 0
    for i in l:
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl
    return max(incl, excl)


def recursion(l: List[int]) -> int:
    if not l:
        return 0
    if len(l) <= 2:
        return max(l)
    return max(
        recursion(l[2:]) + l[0],
        recursion(l[3:]) + l[1]
    )


class TestSolutions(unittest.TestCase):
    def test_recursion(self: 'TestSolutions'):
        self.assertEqual(recursion([6]), 6)
        self.assertEqual(recursion([1, 5]), 5)
        self.assertEqual(recursion([2, 4, 6, 2, 5]), 13)
        self.assertEqual(recursion([5, 1, 1, 5]), 10)

    def test_loop(self: 'TestSolutions'):
        self.assertEqual(loop([6]), 6)
        self.assertEqual(loop([1, 5]), 5)
        self.assertEqual(loop([2, 4, 6, 2, 5]), 13)
        self.assertEqual(loop([5, 1, 1, 5]), 10)


if __name__ == '__main__':
    unittest.main()
