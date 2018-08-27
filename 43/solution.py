"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack,
then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
If there are no elements in the stack,
then it should throw an error or return null.
Each method should run in constant time.
"""
import unittest
from typing import List, Any


class Stack:
    def __init__(self) -> None:
        self.s = []  # type: List[Any]
        self.m = None

    def push(self, val: Any) -> None:
        if not self.m or val > self.m:
            self.m = val
        self.s.append(val)

    def pop(self) -> Any:
        return self.s.pop()

    def max(self) -> Any:
        return self.m


class TestSolution(unittest.TestCase):
    def test_stack(self) -> None:
        s = Stack()
        s.push(10)
        s.push(11)
        s.push(10)
        self.assertEqual(s.max(), 11)
        self.assertEqual(s.pop(), 10)
        self.assertEqual(s.pop(), 11)
        self.assertEqual(s.max(), 10)
        self.assertEqual(s.pop(), 10)
        with self.assertRaises(IndexError):
            s.pop()
        self.assertEqual(s.max(), None)


if __name__ == '__main__':
    unittest.main()
