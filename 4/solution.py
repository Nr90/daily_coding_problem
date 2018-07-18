"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import unittest
from itertools import count, filterfalse
from time import time
from typing import List


def set_deduction(l: List[int]) -> int:
    return min( set(range(1, len(l) + 1)) - set(l) )


def v3(l: List[int]) -> int:
    for i in range(1, len(l) + 1):
        if i not in l:
            return i


def v4(l: List[int]) -> int:
    return next(filterfalse(set(l).__contains__, count(1)))


testcases = [
    ([3, 4, -1, 1], 2),
    ([1, 2, 0], 3),
    ([10, 10, 1, 1, 2, 3], 4),
    ([x if x is not 30 else -1 for x in range(100)], 30)
]


versions = [
    set_deduction,
    v3,
    v4
]


for inp, target in testcases:
    for func in versions:
        start = time()
        for _ in range(1000000):
            func(inp)
        time_needed = time() - start
        print(func, inp, target, func(inp), time_needed)
        assert func(inp) == target
