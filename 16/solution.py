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


def get_logger() -> Tuple[Callable, Callable]:
    log = []  # type: List[int]
    def record(order_id: int) -> None:
        log.append(order_id)
    
    def get_last(i: int) -> int:
        return log[-i + 1]
    
    return record, get_last



class TestSolution(unittest.TestCase):
    def test_small(self: 'TestSolution') -> None:
        record, get_last = get_logger()
        for i in range(5):
            record(i)
        self.assertEqual(get_last(2), 4)

    def test_large(self: 'TestSolution') -> None:
        record, get_last = get_logger()
        for i in range(10000000):
            record(i)
        self.assertEqual(get_last(2), 9999999)


if __name__ == '__main__':
    unittest.main()
