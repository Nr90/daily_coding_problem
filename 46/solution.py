"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""
import unittest


def substring_palindrome(s: str) -> str:
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
