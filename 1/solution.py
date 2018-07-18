"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import unittest
from typing import List


def brute_force(l: List[int], r: int) -> bool:
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            if l[i] + l[j] == r:
                return True
    return False


def set_deduction(l: List[int], r: int) -> bool:
    deducted = set(map(lambda x: r - x, l))
    return bool(deducted.intersection(set(l)))


class TestSolutions(unittest.TestCase):
    def test_brute_force(self: 'TestSolutions'):
        self.assertTrue(brute_force([10, 15, 3, 7], 17))
        self.assertFalse(brute_force([10, 15, 3, 7], 16))

    def test_deduction(self: 'TestSolutions'):
        self.assertTrue(set_deduction([10, 15, 3, 7], 17))
        self.assertFalse(set_deduction([10, 15, 3, 7], 16))


if __name__ == '__main__':
    unittest.main()
