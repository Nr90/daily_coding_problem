"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import unittest
from time import sleep
from threading import Timer
 

def schedule(f, n):
    Timer(n / 1000, f).start()


class TestSolutions(unittest.TestCase):
    def test_func(self: 'TestSolutions'):
        global test
        def func():
            global test
            test = True
        schedule(func, 1000)
        sleep(1.5)
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()
