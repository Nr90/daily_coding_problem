"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
import unittest
from typing import List, Tuple
from collections import Counter


def count_overlaps(intervals: List[Tuple[int, int]]) -> int:
    max_overlaps = 0
    intervals = sorted(intervals, key=(lambda i: i[0]), reverse=True)
    while intervals:
        overlaps = 0
        i = intervals.pop(0)
        for i2 in intervals:
            if i[1] > i2[0]:
                overlaps += 1
        max_overlaps = max(max_overlaps, overlaps)
    return max_overlaps


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        intervals = [(30, 75), (0, 50), (60, 150)]
        self.assertEqual(count_overlaps(intervals), 2)


if __name__ == '__main__':
    unittest.main()
