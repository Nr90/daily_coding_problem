"""
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting
the fewest number of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount
to make a palindrome). There are seven other palindromes that can be made
from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google",
you should return "elgoogle".
"""
import unittest
from typing import Set


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def find_palindrome(s: str) -> str:
    if is_palindrome(s):
        return s
    l = len(s)
    while l > 0:
        for i in range(0, len(s) - l):
            if is_palindrome(s[i:i+l]):
                return s[i+l:][::-1] + s[i:i+l] + s[i+l:]
        l -= 1
    raise Exception("Could not create palindrome")


class TestSolution(unittest.TestCase):
    def test_is_palindrome(self) -> None:
        self.assertTrue(is_palindrome('elgoogle'))
        self.assertFalse(is_palindrome('google'))
        self.assertTrue(is_palindrome('ecarace'))
        self.assertFalse(is_palindrome('race'))

    def test_already_palindrome(self) -> None:
        self.assertEqual(find_palindrome('ecarace'), 'ecarace')

    def test_given_race(self) -> None:
        self.assertEqual(find_palindrome('race'), 'ecarace')

    def test_given_google(self) -> None:
        self.assertEqual(find_palindrome('google'), 'elgoogle')


if __name__ == '__main__':
    unittest.main()
