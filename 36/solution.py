"""
This problem was asked by Dropbox.

Given the root to a binary search tree,
find the second largest node in the tree.
"""
import unittest
from typing import Optional


class BSTN:
    def __init__(self,
                 value: int,
                 left: Optional['BSTN']=None,
                 right: Optional['BSTN']=None) -> None:
        self.left = left
        self.right = right
        self.value = value


def find_second_largest(root: BSTN) -> BSTN:
    current = root
    while current.right and current.right.right:
        current = current.right
    return current


class TestSolution(unittest.TestCase):
    def test_find_second_largest_small(self) -> None:
        r"""
          3
         / \
        1   5
        """
        root = BSTN(3, BSTN(1), BSTN(5))
        second_largest = find_second_largest(root)
        self.assertEqual(second_largest.value, 3)

    def test_find_second_largest_uneven(self) -> None:
        r"""
        Tree used for test:
              17
             /  \
            /    \
           /      \
          5       35
         / \     /  \
        2   16  29  38
               /  \
              19  33
        """
        root = BSTN(
            17,
            BSTN(5, BSTN(2), BSTN(16)),
            BSTN(35, BSTN(29, BSTN(19), BSTN(33)), BSTN(38)))
        second_largest = find_second_largest(root)
        self.assertEqual(second_largest.value, 35)

    def test_find_second_largest_even(self) -> None:
        r"""
        Tree used for test:
              17
             /  \
            /    \
           /      \
          5       35
         / \     /  \
        2   16  29  38
        """
        root = BSTN(
            17,
            BSTN(5, BSTN(2), BSTN(16)),
            BSTN(35, BSTN(29), BSTN(38)))
        second_largest = find_second_largest(root)
        self.assertEqual(second_largest.value, 35)


if __name__ == '__main__':
    unittest.main()
