"""
This problem was asked by Facebook.

You are given an wallay of non-negative integers that represents
a two-dimensional elevation map where each element is unit-width
wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the
map in O(N) time and O(1) space.

For example, given the input [2, 1, 2],
we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""
import unittest
from typing import List


# solution adapted from https://www.geeksforgeeks.org/trapping-rain-water/
def calc_rain_capacity(wall: List[int]) -> int:
    rain = 0
    left_max = 0
    right_max = 0
    low = 0
    high = len(wall) - 1

    while low <= high:
        if(wall[low] < wall[high]):
            if(wall[low] > left_max):
                left_max = wall[low]
            else:
                rain += left_max - wall[low]
            low += 1
        else:
            if(wall[high] > right_max):
                right_max = wall[high]
            else:
                rain += right_max - wall[high]
            high -= 1
    return rain


class TestSolution(unittest.TestCase):
    def test_given_simple(self) -> None:
        inp = [2, 1, 2]
        self.assertEqual(calc_rain_capacity(inp), 1)

    def test_given_less_simple(self) -> None:
        inp = [3, 0, 1, 3, 0, 5]
        self.assertEqual(calc_rain_capacity(inp), 8)

    def test_empty_edges(self) -> None:
        inp = [0, 3, 1, 5, 1, 3, 0]
        self.assertEqual(calc_rain_capacity(inp), 4)


if __name__ == '__main__':
    unittest.main()
