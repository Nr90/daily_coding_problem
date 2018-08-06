"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond]
or ['bedbath', 'and', 'beyond'].
"""
import unittest
from typing import List, Optional


def reconstruct(words: List[str], s: str, reconstruction: List[str]=[]) -> Optional[List[str]]:
    if not s:
        return reconstruction
    for w in words:
        w_len = len(w)
        if w_len <= len(s) and w == s[:w_len]:
            r = reconstruct(words, s[w_len:], reconstruction + [w])
            if r is not None:
                return r
    return None


class TestSolution(unittest.TestCase):
    def test_empty_string(self) -> None:
        words = []  # type: List[str]
        s = ''
        expected = []  # type: List[str]
        self.assertEqual(reconstruct(words, s), expected)

    def test_given1(self) -> None:
        words = ['quick', 'brown', 'the', 'fox']
        s = 'thequickbrownfox'
        expected = ['the', 'quick', 'brown', 'fox']
        self.assertEqual(reconstruct(words, s), expected)

    def test_given2(self) -> None:
        words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
        s = 'bedbathandbeyond'
        expectations = [
            ['bedbath', 'and', 'beyond'],
            ['bed', 'bath', 'and', 'beyond']
        ]
        self.assertTrue(
            reconstruct(words, s) in expectations
        )

    def test_no_reconstruction(self) -> None:
        words = ['brown', 'the', 'fox']
        s = 'thequickbrownfox'
        expected = None
        self.assertEqual(reconstruct(words, s), expected)


if __name__ == '__main__':
    unittest.main()
