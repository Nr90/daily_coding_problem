"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""
import unittest
from typing import List
from contextlib import contextmanager
from io import StringIO
import sys
from collections import deque


def window_max(arr: List[int], k: int) -> None:
    d = deque()
    for i, val in enumerate(arr):
        while len(d) > 0 and val > d[-1]:
            d.pop()
        d.append(val)
        start = i - k + 1
        if start >= 0:
            print(d[0])
            if arr[start] == d[0]:
                d.popleft()


@contextmanager
def captured_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        with captured_output() as out:
            window_max([10, 5, 2, 7, 8, 7], 3)
        self.assertEqual(out.getvalue(), '10\n7\n8\n8\n')


if __name__ == '__main__':
    unittest.main()
