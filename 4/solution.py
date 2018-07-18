from typing import List
from functools import reduce
from itertools import count, filterfalse
from time import time


def v1(l: List[int]) -> int:
    potential_ints = set(range(1, len(l) + 1))
    for i in l:
        potential_ints.discard(i)
    return min(potential_ints)


def v2(l: List[int]) -> int:
    return min( set(range(1, len(l) + 1)) - set(l) )


def v3(l: List[int]) -> int:
    for i in range(1, len(l) + 1):
        if i not in l:
            return i


def v4(l: List[int]) -> int:
    potential_ints = list(range(1, len(l) + 1))
    for i in l:
        try:
            potential_ints.remove(i)
        except ValueError:
            continue
    return min(potential_ints)


def v5(l: List[int]) -> int:
    return next(filterfalse(set(l).__contains__, count(1)))


testcases = [
    ([3, 4, -1, 1], 2),
    ([1, 2, 0], 3),
    ([10, 10, 1, 1, 2, 3], 4),
    ([x if x is not 30 else -1 for x in range(100)], 30)
]


versions = [
    v1,
    v2,
    v3,
    v4,
    v5
]


for inp, target in testcases:
    for func in versions:
        start = time()
        for _ in range(1000000):
            func(inp)
        time_needed = time() - start
        print(func, inp, target, func(inp), time_needed)
        assert func(inp) == target
