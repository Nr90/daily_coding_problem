"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import unittest
from typing import List
import random


def get_random_elem(stream):
    r = None
    for i, e in enumerate(stream):
        if i == 0:
            r = e
        elif random.randint(1, i + 1) == 1:
            r = e
    return r


class TestSolution(unittest.TestCase):
    def test_given_example(self: 'TestSolution') -> None:
        stream = [1, 2, 3]
        self.assertTrue(get_random_elem(stream) in stream)


if __name__ == '__main__':
    unittest.main()
