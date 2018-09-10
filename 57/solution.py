"""
This problem was asked by Amazon.

Given a string s and an integer k,
break up the string into multiple texts
such that each text has a length of k or less.
You must break it up so that words don't break across lines.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and
that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog"
and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10.
"""
import unittest
from typing import List, Optional


def break_up(s: str, k: int) -> Optional[List[str]]:
    lines = []
    while ' ' in s:
        last_space = 0
        for i in range(len(s)):
            if i > k:
                break
            if s[i] == ' ':
                last_space = i
        if not last_space:
            return None
        lines.append(s[0:last_space])
        s = s[last_space+1:]
    if len(s) <= k:
        lines.append(s)
    else:
        return None
    return lines


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        s = 'the quick brown fox jumps over the lazy dog'
        k = 10
        self.assertEqual(
            break_up(s, k),
            ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']
        )


if __name__ == '__main__':
    unittest.main()
