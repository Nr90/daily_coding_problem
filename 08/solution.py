"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
import unittest
from typing import Optional


class BinaryTreeNode:
    def __init__(self: 'BinaryTreeNode',
                 value: int, left: Optional['BinaryTreeNode']=None,
                 right: Optional['BinaryTreeNode']=None) -> None:
        self.value = value
        self.left = left
        self.right = right
    
    def is_unival(self: 'BinaryTreeNode') -> bool:
        return unival_rec(self, self.value)


def count_unival_subtrees(root: Optional[BinaryTreeNode]) -> int:
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if root.is_unival() else left + right


def unival_rec(root: Optional[BinaryTreeNode], value: int) -> bool:
    if root is None:
        return True
    if root.value == value:
        return unival_rec(root.left, value) and unival_rec(root.right, value)
    return False


class TestSolutions(unittest.TestCase):
    def test_count_unival_subtrees(self: 'TestSolutions'):
        root = BinaryTreeNode(0, 
            left=BinaryTreeNode(1),
            right=BinaryTreeNode(0,
                left=BinaryTreeNode(1,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(1)),
                right=BinaryTreeNode(0)))
        self.assertEqual(count_unival_subtrees(root), 5)


if __name__ == '__main__':
    unittest.main()
