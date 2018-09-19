"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""
import unittest
from typing import Iterator


def gen_substrings(s: str) -> Iterator[str]:
    n = len(s)
    for length in range(n, 0, -1):
        for start in range(n-length+1):
            yield s[start:start+length]


def check_palindrome(s: str) -> bool:
    return s == s[::-1]


def substring_palindrome(s: str) -> str:
    for sub_s in gen_substrings(s):
        if check_palindrome(sub_s):
            return sub_s
    return ''


class TestSolution(unittest.TestCase):
    def test_given_aabcdcb(self) -> None:
        self.assertEqual(
            substring_palindrome('aabcdcb'),
            'bcdcb')

    def test_given_bananas(self) -> None:
        self.assertEqual(
            substring_palindrome('bananas'),
            'anana')


if __name__ == '__main__':
    unittest.main()
