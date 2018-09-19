"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n,
and contain the following methods:

set(key, value): sets key to value.
    If there are already n items in the cache and we are adding a new item,
    then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""
import unittest
from collections import OrderedDict
from typing import Any


class LRUCache:
    def __init__(self, n: int) -> None:
        self.n = n
        self.cache = OrderedDict()  # type: OrderedDict[Any, Any]
        self.items = 0

    def get(self, key: Any) -> Any:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return None

    def set(self, key: Any, value: Any) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            self.items += 1
            if self.items > self.n:
                self.cache.popitem(last=False)
        self.cache[key] = value


class TestSolution(unittest.TestCase):
    def test_set_and_get(self) -> None:
        lruc = LRUCache(5)
        self.assertEqual(lruc.get('1'), None)
        lruc.set('1', 1)
        self.assertEqual(lruc.get('1'), 1)
        lruc.set('2', 2)
        lruc.set('3', 3)
        lruc.set('4', 4)
        lruc.set('5', 5)
        lruc.set('6', 6)
        self.assertEqual(lruc.get('1'), None)


if __name__ == '__main__':
    unittest.main()
