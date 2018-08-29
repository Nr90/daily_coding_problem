"""
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive)
with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import unittest
from random import randint


def rand5() -> int:
    return randint(1, 5)


def rand7() -> int:
    return 1


class TestSolution(unittest.TestCase):
    def test_rand7(self) -> None:
        dist = [0 for _ in range(0, 7)]
        for _ in range(700):
            i = rand7()
            dist[i-1] += 1
            self.assertTrue(i >= 1 and i <= 7)
        for d in dist:
            self.assertAlmostEqual(1, d / 100, places=0)


if __name__ == '__main__':
    unittest.main()
