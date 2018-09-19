"""
This problem was asked by Apple.

Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods:
    enqueue, which inserts an element into the queue, and
    dequeue, which removes it.
"""
import unittest
from typing import Any, List


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, elem: Any) -> None:
        self.stack1.append(elem)

    def dequeue(self) -> Any:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


class TestSolution(unittest.TestCase):
    def test_queue(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)


if __name__ == '__main__':
    unittest.main()
