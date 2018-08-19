"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers.
That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the
average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5],
your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from typing import List
from statistics import median


@contextmanager
def captured_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


def running_mean(seq: List[int]) -> None:
    for i in range(1, len(seq) + 1):
        print('%g' % median(seq[:i]))


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        with captured_output() as out:
            running_mean([2, 1, 5, 7, 2, 0, 5])
        self.assertEqual(out.getvalue(), '2\n1.5\n2\n3.5\n2\n2\n2\n')


if __name__ == '__main__':
    unittest.main()
