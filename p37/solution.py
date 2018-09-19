"""
This problem was asked by Google.

The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""
import unittest
from itertools import chain, combinations
from typing import List, Set


def powerset(s: Set[int]) -> List[Set[int]]:
    return list(map(set, chain.from_iterable(
        combinations(s, r) for r in range(len(s)+1))))


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(
            powerset({1, 2, 3}),
            [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
        )


if __name__ == '__main__':
    unittest.main()
