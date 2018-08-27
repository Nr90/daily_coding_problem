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
        self.stack = []  # type: List[Any]
        self.max_stack = []  # type: List[Any]

    def push(self, val: Any) -> None:
        if not self.stack:
            self.stack.append(val)
            self.max_stack.append(val)
        else:
            self.stack.append(val)
            if val > self.max_stack[-1]:
                self.max_stack.append(val)
            else:
                self.max_stack.append(self.max_stack[-1])

    def pop(self) -> Any:
        val = self.stack.pop()
        self.max_stack.pop()
        return val

    def max(self) -> Any:
        return self.max_stack[-1]


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
        with self.assertRaises(IndexError):
            s.max()


if __name__ == '__main__':
    unittest.main()
