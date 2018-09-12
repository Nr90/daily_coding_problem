"""
This problem was asked by Facebook.

Given a multiset of integers,
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35},
which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
import unittest
from typing import List
from itertools import combinations


def subsets_same_sum_exist(s: List[int]) -> bool:
    if sum(s) % 2:
        return False
    for l in range(1, len(s)):
        for sub_s in combinations(s, l):
            if sum(sub_s) == sum(filter(lambda x: x not in sub_s, s)):
                return True
    return False


class TestSolution(unittest.TestCase):
    def test_given_true(self) -> None:
        multiset = [15, 5, 20, 10, 35, 15, 10]
        self.assertTrue(subsets_same_sum_exist(multiset))

    def test_given_false(self) -> None:
        multiset = [15, 5, 20, 10, 35]
        self.assertFalse(subsets_same_sum_exist(multiset))


if __name__ == '__main__':
    unittest.main()
