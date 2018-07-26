"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
import unittest
from typing import Set
 

def count_unique_ways(N: int) -> int:
    if N <= 1:
        return 1
    return count_unique_ways(N-2) + count_unique_ways(N-1)


def count_unique_ways_with_steps(N: int, steps: Set[int]) -> int:
    if N == 0:
        return 1
    if min(steps) > N:
        return 0
    ways = 0
    for s in steps:
        ways += count_unique_ways_with_steps(N-s, steps)
    return ways



class TestSolutions(unittest.TestCase):
    def test_one_step(self: 'TestSolutions') -> None:
        self.assertEqual(count_unique_ways(1), 1)

    def test_given_example(self: 'TestSolutions') -> None:
        self.assertEqual(count_unique_ways(4), 5)

    def test_given_example_with_steps(self: 'TestSolutions') -> None:
        self.assertEqual(count_unique_ways_with_steps(4, {1, 2}), 5)

    def test_given_example_with_more_steps(self: 'TestSolutions') -> None:
        self.assertEqual(count_unique_ways_with_steps(4, {1, 3, 5}), 3)


if __name__ == '__main__':
    unittest.main()
