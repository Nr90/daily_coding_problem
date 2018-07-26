"""
This problem was asked by Twitter.

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that s as a prefix.

For example, given the query string de and the set of strings [door, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
import unittest
from typing import List, Iterator
 

class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = {}

    def add(self, word):
        if not word:
            return
        l = word[0]
        if l not in self.children:
            self.children[l] = TrieNode(l)
        self.children[l].add(word[1:])

    def get_with_prefix(self, prefix):
        if not prefix:
            return self
        if prefix[0] not in self.children:
            return None
        return self.children[prefix[0]].get_with_prefix(prefix[1:])
    
    def get_child_words(self):
        if len(self.children) == 0:
            return [self.char]
        child_words = []
        for c in self.children.values():
            child_words += [self.char + w for w  in c.get_child_words()]
        return child_words


def trie_autocomplete(s: str, possible: List[str]) -> Iterator[str]:
    root = TrieNode()
    for w in possible:
        root.add(w)
    head = root.get_with_prefix(s)
    if not head:
        return []
    return [s[:-1] + w for w in head.get_child_words()]


class TestSolutions(unittest.TestCase):
    def test_empty_query(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(trie_autocomplete('', ['door', 'deer', 'deal'])),
            sorted(['door', 'deer', 'deal'])
        )

    def test_non_matching_query(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(trie_autocomplete('elbert', ['door', 'deer', 'deal'])),
            sorted([])
        )

    def test_given_example(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(trie_autocomplete('de', ['door', 'deer', 'deal'])),
            sorted(['deer', 'deal'])
        )


if __name__ == '__main__':
    unittest.main()
