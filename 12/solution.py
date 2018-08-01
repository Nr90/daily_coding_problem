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
    a, b = 1, 2
    for _ in range(N - 1):
        a, b = b, a + b
    return a


def count_unique_ways_with_steps(N: int, steps: Set[int]) -> int:
    cache = [0 for _ in range(N + 1)]
    cache[0] = 1
    for i in range(1, N + 1):
        cache[i] += sum(cache[i - x] for x in steps if i - x >= 0)
    return cache[N]


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
