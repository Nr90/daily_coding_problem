"""
This problem was asked by Stripe.

Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import unittest
from itertools import count, filterfalse
from time import time
from typing import List


def set_deduction(l: List[int]) -> int:
    return min(set(range(1, len(l) + 1)) - set(l))


def loop(l: List[int]) -> int:
    for i in range(1, len(l) + 1):
        if i not in l:
            return i
    raise Exception("Failed to find a solution")


def ffalse(l: List[int]) -> int:
    return next(filterfalse(set(l).__contains__, count(1)))


class TestSolutions(unittest.TestCase):
    def test_division(self: 'TestSolutions'):
        self.assertEqual(set_deduction([3, 4, -1, 1]), 2)
        self.assertEqual(set_deduction([1, 2, 0]), 3)

    def test_loop(self: 'TestSolutions'):
        self.assertEqual(loop([3, 4, -1, 1]), 2)
        self.assertEqual(loop([1, 2, 0]), 3)

    def test_ffalse(self: 'TestSolutions'):
        self.assertEqual(ffalse([3, 4, -1, 1]), 2)
        self.assertEqual(ffalse([1, 2, 0]), 3)


if __name__ == '__main__':
    unittest.main()
