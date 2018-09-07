"""
This problem was asked by Amazon.

Given an array of numbers,
find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9],
the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""
import unittest
from typing import List


def max_sub_sum(arr: List[int]) -> int:
    n = len(arr)
    solution = [0] * n
    solution[0] = arr[0]
    for i in range(1, n):
        solution[i] = max(solution[i-1]+arr[i], arr[i])
    return max(solution + [0])


class TestSolution(unittest.TestCase):
    def test_given_mixed(self) -> None:
        self.assertEqual(max_sub_sum([34, -50, 42, 14, -5, 86]), 137)

    def test_given_all_negative(self) -> None:
        self.assertEqual(max_sub_sum([-5, -1, -8, -9]), 0)


if __name__ == '__main__':
    unittest.main()
