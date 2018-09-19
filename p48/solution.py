r"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""
import unittest
from typing import List, Optional


class BinTreeNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.left = None  # type: Optional['BinTreeNode']
        self.right = None  # type: Optional['BinTreeNode']


# Solution inspired by:
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
def reconstruct_tree(preorder: List[str],
                     inorder: List[str]) -> Optional[BinTreeNode]:
    preorder_iter = iter(preorder)

    def reconstruct(in_start: int, in_end: int) -> Optional[BinTreeNode]:
        if in_start > in_end:
            return None
        v = next(preorder_iter, None)
        if not v:
            return None
        node = BinTreeNode(v)
        in_index = inorder.index(node.val)
        node.left = reconstruct(in_start, in_index-1)
        node.right = reconstruct(in_index+1, in_end)
        return node
    return reconstruct(0, len(inorder))


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
        inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
        tree = reconstruct_tree(preorder, inorder)
        self.assertIsNotNone(tree)
        assert tree
        self.assertEqual(tree.val, 'a')
        assert tree.left
        self.assertEqual(tree.left.val, 'b')
        assert tree.left.left
        self.assertEqual(tree.left.left.val, 'd')
        assert tree.left.right
        self.assertEqual(tree.left.right.val, 'e')
        assert tree.right
        self.assertEqual(tree.right.val, 'c')
        assert tree.right.left
        self.assertEqual(tree.right.left.val, 'f')
        assert tree.right.right
        self.assertEqual(tree.right.right.val, 'g')


if __name__ == '__main__':
    unittest.main()
