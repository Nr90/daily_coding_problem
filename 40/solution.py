"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except
for one integer, which only occurs once,
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
import unittest
from typing import List
import ctypes


# solution reimplemented based on:
# https://www.geeksforgeeks.org/find-the-element-that-appears-once/
def unique(arr: List[int]) -> int:
    result = 0
    # for every bit
    for i in range(ctypes.sizeof(ctypes.c_void_p) * 8):
        count = 0
        # shift bit of 1 to the left i times, so we operate on the ith bit
        x = 1 << i
        # count the amount of times the bit was set to 1 in the array
        for e in arr:
            if e & x:
                count += 1
        # if the count of the bits modelo 3 is not 0,
        # add the bit to result using OR
        if count % 3:
            result = result | x
    return result


class TestSolution(unittest.TestCase):
    def test_given_7(self) -> None:
        self.assertEqual(
            unique([6, 1, 3, 3, 3, 6, 6]),
            1)

    def test_given_4(self) -> None:
        self.assertEqual(
            unique([13, 19, 13, 13]),
            19)


if __name__ == '__main__':
    unittest.main()
