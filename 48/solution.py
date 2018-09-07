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


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
