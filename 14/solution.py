"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import unittest
from typing import List
from random import random
import math
 

def calc_pi() -> float:
    inside = 0
    total = 100000000

    for i in range(0, total):
        x2 = random() ** 2
        y2 = random() ** 2
        # Increment if inside unit circle.
        if math.sqrt(x2 + y2) < 1.0:
            inside += 1
    return round(inside / total * 4, 3)


class TestSolution(unittest.TestCase):
    def test_given_example(self: 'TestSolution') -> None:
        self.assertAlmostEqual(calc_pi(), 3.142)


if __name__ == '__main__':
    unittest.main()
