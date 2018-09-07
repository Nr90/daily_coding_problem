r"""
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""
import unittest
from typing import Optional


class InternalNode:
    def __init__(self,
                 op: str,
                 lchild_leaf: Optional[int] = None,
                 rchild_leaf: Optional[int] = None,
                 lchild_int: Optional['InternalNode'] = None,
                 rchild_int: Optional['InternalNode'] = None) -> None:
        self.op = op
        self.lchild_leaf = lchild_leaf
        self.rchild_leaf = rchild_leaf
        self.lchild_int = lchild_int
        self.rchild_int = rchild_int


def calc(head: InternalNode) -> int:
    if not head.lchild_int or not head.rchild_int:
        return eval(f'{head.lchild_leaf} {head.op} {head.rchild_leaf}')
    return eval(f'{calc(head.lchild_int)} {head.op} {calc(head.rchild_int)}')


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        head = InternalNode(
            op='*',
            lchild_int=InternalNode('+', lchild_leaf=3, rchild_leaf=2),
            rchild_int=InternalNode('+', lchild_leaf=4, rchild_leaf=5)
        )
        self.assertEqual(calc(head), 45)

    def test_depth1(self) -> None:
        head = InternalNode(
            op='*',
            lchild_leaf=3,
            rchild_leaf=6
        )
        self.assertEqual(calc(head), 18)


if __name__ == '__main__':
    unittest.main()
