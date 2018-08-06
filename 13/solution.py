"""
This problem was asked by Amazon.

Given an integer k and a string s,
find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".
"""
import unittest
from typing import List


def is_valid(s: str, k: int) -> bool:
    return len(set(s)) <= k


def longest_substring_k_chars(s: str, k: int) -> str:
    s_len = len(s)
    while s_len > 0:
        start_indices = range(len(s) - s_len + 1)
        for i in start_indices:
            if is_valid(s[i:i+s_len], k):
                return s[i:i+s_len]
        s_len -= 1
    raise Exception('could not generate a valid substring')


class TestSolution(unittest.TestCase):
    def test_given_example(self: 'TestSolution') -> None:
        self.assertEqual(longest_substring_k_chars('abcba', 2), 'bcb')

    def test_full_string(self: 'TestSolution') -> None:
        self.assertEqual(longest_substring_k_chars('abcba', 3), 'abcba')


if __name__ == '__main__':
    unittest.main()
