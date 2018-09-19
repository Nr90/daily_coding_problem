"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The edit distance between two strings refers to the minimum
number of character insertions, deletions, and substitutions
required to change one string to the other. For example,
the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
import unittest
from functools import lru_cache


@lru_cache()
def levenshtein(s1: str, s2: str) -> int:
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    cost = 0 if s1[-1] == s2[-1] else 1
    return min([levenshtein(s1[:-1], s2) + 1,
               levenshtein(s1, s2[:-1]) + 1,
               levenshtein(s1[:-1], s2[:-1]) + cost])


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(levenshtein('kitten', 'sitting'), 3)


if __name__ == '__main__':
    unittest.main()
