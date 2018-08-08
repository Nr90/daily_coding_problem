"""
This problem was asked by Google.

Implement locking in a binary tree.
A binary tree node can be locked or unlocked only if
all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked

lock, which attempts to lock the node. If it cannot be locked,
    then it should return false.
    Otherwise, it should lock it and return true.

unlock, which unlocks the node. If it cannot be unlocked,
    then it should return false.
    Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or
any other property you would like.
You may assume the class is used in a single-threaded program,
so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
"""
import unittest
from typing import Optional


class BinaryTreeNode:
    def __init__(self) -> None:
        self.parent = None  # type: Optional[BinaryTreeNode]
        self.lchild = None  # type: Optional[BinaryTreeNode]
        self.rchild = None  # type: Optional[BinaryTreeNode]
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked

    def lock(self) -> bool:
        if self.is_changeable():
            self.locked = True
            return True
        return False

    def unlock(self) -> bool:
        if self.is_changeable():
            self.locked = False
            return True
        return False

    def has_locked_parents(self) -> bool:
        if not self.parent:
            return False
        if self.parent.is_locked():
            return True
        return self.parent.has_locked_parents()

    def has_locked_children(self) -> bool:
        if self.lchild and (self.lchild.is_locked() or
                            self.lchild.has_locked_children()):
            return True
        if self.rchild and (self.rchild.is_locked() or
                            self.rchild.has_locked_children()):
            return True
        return False

    def is_changeable(self) -> bool:
        return not self.has_locked_children() and not self.has_locked_parents()


class TestSolution(unittest.TestCase):
    r"""
    Binary Tree we will test with:
            A
           / \
          /   \
         B     C
        / \   / \
       D   E F   G
    """

    def setUp(self) -> None:
        self.tree = {
            n: BinaryTreeNode() for n in ['A', 'B', 'C', 'D', 'E', 'F', 'G']}
        self.tree['A'].lchild = self.tree['B']
        self.tree['A'].rchild = self.tree['C']
        self.tree['B'].parent = self.tree['A']
        self.tree['B'].lchild = self.tree['D']
        self.tree['B'].rchild = self.tree['E']
        self.tree['C'].parent = self.tree['A']
        self.tree['C'].lchild = self.tree['F']
        self.tree['C'].rchild = self.tree['G']
        self.tree['D'].parent = self.tree['B']
        self.tree['E'].parent = self.tree['B']
        self.tree['F'].parent = self.tree['C']
        self.tree['G'].parent = self.tree['C']

    def test_lock_parent(self) -> None:
        self.assertTrue(self.tree['A'].lock())
        self.assertFalse(self.tree['B'].lock())
        self.assertFalse(self.tree['F'].lock())

    def test_lock_child(self) -> None:
        self.assertTrue(self.tree['G'].lock())
        self.assertFalse(self.tree['C'].lock())
        self.assertFalse(self.tree['A'].lock())

    def test_is_locked(self) -> None:
        self.assertFalse(self.tree['A'].is_locked())
        self.assertTrue(self.tree['A'].lock())
        self.assertTrue(self.tree['A'].is_locked())

    def test_unlock_self(self) -> None:
        self.assertTrue(self.tree['A'].lock())
        self.assertTrue(self.tree['A'].unlock())

    def test_unlock_parent(self) -> None:
        self.assertTrue(self.tree['A'].lock())
        self.tree['B'].locked = True
        self.assertFalse(self.tree['B'].unlock())

    def test_unlock_child(self) -> None:
        self.assertTrue(self.tree['G'].lock())
        self.tree['C'].locked = True
        self.assertFalse(self.tree['C'].unlock())


if __name__ == '__main__':
    unittest.main()
