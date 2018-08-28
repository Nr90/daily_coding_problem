"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the
number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has.
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions:
    every distinct pair forms an inversion.
"""
import unittest
from typing import List


def count_inversions(arr: List[int]) -> int:
    return 0


class TestSolution(unittest.TestCase):
    def test_count_inversions_sorted(self) -> None:
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversions(arr), 0)

    def test_count_inversions_three(self) -> None:
        arr = [2, 4, 1, 3, 5]
        self.assertEqual(count_inversions(arr), 3)

    def test_count_inversions_ten(self) -> None:
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversions(arr), 10)


if __name__ == '__main__':
    unittest.main()
