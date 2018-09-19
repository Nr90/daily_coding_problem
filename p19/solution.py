"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses
that can be of K different colors.
He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""
import unittest
from math import inf
from typing import List, Optional


def min_cost(matrix: List[List[float]],
             prev_color: Optional[int]=None) -> float:
    if len(matrix) == 1:
        if prev_color is None:
            return min(matrix[0])
        return min(matrix[0][:prev_color] + matrix[0][(prev_color + 1):])
    cost = inf
    for i, r in enumerate(matrix):
        if i != prev_color:
            cost = min(cost, r[i] + min_cost(matrix[1:], i))
    return cost


class TestSolution(unittest.TestCase):
    def test_one_house(self) -> None:
        cost_m = [[5.0, 8.0, 3.0]]
        self.assertEqual(min_cost(cost_m), 3.0)

    def test_two_houses_two_colors(self) -> None:
        cost_m = [[5.0, 8.0], [8.0, 5.0]]
        self.assertEqual(min_cost(cost_m), 10.0)


if __name__ == '__main__':
    unittest.main()
