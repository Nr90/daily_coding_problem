"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
import unittest
from collections import deque
from typing import Deque


def check_balance(s: str) -> bool:
    cq = deque()  # type: Deque[str]
    for c in s:
        if c is '[' or c is '{' or c is '(':
            cq.append(c)
            continue
        if not cq:
            return False
        if c is ']' and cq[-1] is not '[':
            return False
        if c is '}' and cq[-1] is not '{':
            return False
        if c is ')' and cq[-1] is not '(':
            return False
        cq.pop()
    return not bool(cq)


class TestSolution(unittest.TestCase):
    def test_given_true(self) -> None:
        self.assertTrue(check_balance(r'([])[]({})'))

    def test_given_false(self) -> None:
        self.assertFalse(check_balance(r'([)]'))

    def test_only_open(self) -> None:
        self.assertFalse(check_balance(r'('))

    def test_only_close(self) -> None:
        self.assertFalse(check_balance(r')'))


if __name__ == '__main__':
    unittest.main()
