"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""
import unittest
from typing import Callable, List, Tuple
import numpy as np


class Logger:
    def __init__(self, N: int) -> None:
        self.log = np.empty([N], dtype=int)
        self.last = 0

    def record(self, order_id: int) -> None:
        self.log[self.last] = order_id
        self.last += 1
    
    def get_last(self, i: int) -> int:
        return self.log[self.last-i]


class TestSolution(unittest.TestCase):
    def test_small(self: 'TestSolution') -> None:
        l = Logger(5)
        for i in range(5):
            l.record(i)
        self.assertEqual(l.get_last(1), 4)

    def test_large(self: 'TestSolution') -> None:
        n = 10000000
        l = Logger(n)
        for i in range(n):
            l.record(i)
        self.assertEqual(l.get_last(1), 9999999)


if __name__ == '__main__':
    unittest.main()
