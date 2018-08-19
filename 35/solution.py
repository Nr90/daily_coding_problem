"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last.
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
import unittest
from typing import List


def count_sort(arr: List[str]) -> List[str]:
    return arr


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        inp = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
        out = ['R', 'R', 'R', 'G', 'G', 'B', 'B']
        self.assertEqual(count_sort(inp), out)


if __name__ == '__main__':
    unittest.main()
