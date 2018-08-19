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
from collections import defaultdict
import unittest
from typing import List, Dict


def count_sort(arr: List[str]):
    counts = defaultdict(lambda: 0)  # type: Dict[str, int]
    for e in arr:
        counts[e] += 1
    ri = 0
    gi = counts['R']
    bi = counts['R'] + counts['G']
    for i in range(ri, counts['R']):
        if arr[i] is 'G':
            arr[i], arr[gi] = arr[gi], arr[i]
            gi += 1
        if arr[i] is 'B':
            arr[i], arr[bi] = arr[bi], arr[i]
            bi += 1
    for i in range(gi, counts['R'] + counts['G']):
        if arr[i] is 'R':
            arr[i], arr[ri] = arr[ri], arr[i]
        if arr[i] is 'B':
            arr[i], arr[bi] = arr[bi], arr[i]


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        inp = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
        count_sort(inp)
        out = ['R', 'R', 'R', 'G', 'G', 'B', 'B']
        self.assertEqual(inp, out)


if __name__ == '__main__':
    unittest.main()
