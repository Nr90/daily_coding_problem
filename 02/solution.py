"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import unittest
from functools import reduce
from typing import List


def division(l: List[int]) -> List[int]:
    s = reduce(lambda x, y: x * y, l)
    return [s // v for v in l]


def double_loop(l: List[int]) -> List[int]:
    r = []
    for i in range(len(l)):
        s = 1
        for j, v in enumerate(l):
            if i != j:
                s *= v
        r.append(s)
    return r


class TestSolutions(unittest.TestCase):
    def test_division(self: 'TestSolutions'):
        self.assertEqual(division([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(division([3, 2, 1]), [2, 3, 6])
        self.assertEqual(division([2, 2, 1]), [2, 2, 4])

    def test_double_loop(self: 'TestSolutions'):
        self.assertEqual(double_loop([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(double_loop([3, 2, 1]), [2, 3, 6])
        self.assertEqual(double_loop([2, 2, 1]), [2, 2, 4])


if __name__ == '__main__':
    unittest.main()
