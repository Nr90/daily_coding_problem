"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
"""
import unittest
from threading import Timer
from time import sleep
from typing import Callable


def schedule(f: Callable, n: int) -> None:
    Timer(n / 1000, f).start()


class TestSolutions(unittest.TestCase):
    def test_func(self: 'TestSolutions') -> None:
        self.test = False

        def func():
            self.test = True
        schedule(func, 1000)
        sleep(1.5)
        self.assertTrue(self.test)


if __name__ == '__main__':
    unittest.main()
