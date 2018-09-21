"""
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache.
It should be able to be initialized with a cache size n,
and contain the following methods:

    set(key, value): sets key to value.
        If there are already n items in the cache and we are adding a new item,
        then it should also remove the least frequently used item.
        If there is a tie, then the least recently used key should be removed.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""
import unittest
from collections import defaultdict
from typing import Any, Dict, List, Optional


class Item:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self._value = value
        self.uses = 0

    @property
    def value(self) -> Any:
        self.uses += 1
        return self._value


class LFUCache:
    def __init__(self, n: int) -> None:
        self.n = n
        self.items = []  # type: List[Item]
        self.lookup = defaultdict(
            lambda: None)  # type: Dict[Any, Optional[int]]

    def get(self, key: Any) -> Any:
        idx = self.lookup[key]
        if idx is None:
            return None
        item = self.items[idx].value
        if idx > 0 and self.items[idx].uses >= self.items[idx-1].uses:
            self.items[idx], self.items[idx-1] = \
                self.items[idx-1], self.items[idx]
        return item

    def set(self, key: Any, value: Any) -> None:
        n_items = len(self.items)
        if n_items == self.n:
            self.lookup.pop(self.items.pop().key)
        self.items.append(Item(key, value))
        self.lookup[key] = n_items


class TestSolution(unittest.TestCase):
    def test_set_and_get(self) -> None:
        lfuc = LFUCache(3)
        self.assertIsNone(lfuc.get('1'))
        lfuc.set('1', 1)
        self.assertEqual(lfuc.get('1'), 1)
        lfuc.set('2', 2)
        self.assertEqual(lfuc.get('2'), 2)
        lfuc.set('3', 3)
        lfuc.set('4', 4)
        self.assertIsNone(lfuc.get('3'))


if __name__ == '__main__':
    unittest.main()
