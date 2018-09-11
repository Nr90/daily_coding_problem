"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array,
find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""
import unittest
from typing import List


def find(arr: List[int], k: int, l: int=0, h: int=-1) -> int:
    if h == -1:
        h = len(arr) - 1

    pivot = (l + h) // 2
    if arr[pivot] == k:
        return pivot

    # if left of pivot is sorted
    if arr[l] <= arr[pivot]:
        # check if k is in left half
        if k >= arr[l] and k <= arr[pivot]:
            return find(arr, k, l, pivot-1)
        # find k in right half
        return find(arr, k, pivot+1, h)

    # then right half is sorted
    # check if key is in right half
    if k >= arr[pivot] and k <= arr[h]:
        return find(arr, k, pivot+1, h)
    # find key in left half
    return find(arr, k, l, pivot-1)


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        arr = [13, 18, 25, 2, 8, 10]
        self.assertEqual(find(arr, 8), 4)


if __name__ == '__main__':
    unittest.main()
