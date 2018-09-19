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


# https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0
def merge_sort_inversions(arr: List[int]):
    if len(arr) == 1:
        return arr, 0

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    left, left_inv = merge_sort_inversions(left)
    right, right_inv = merge_sort_inversions(right)
    inversions = 0 + left_inv + right_inv

    combined = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
            inversions += len(left) - i
    combined += left[i:]
    combined += right[j:]
    return combined, inversions


def count_inversions(arr: List[int]) -> int:
    _, inversions = merge_sort_inversions(arr)
    return inversions


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
