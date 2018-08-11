'''
This problem was asked by Palantir.

Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line,
then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
and k = 16, you should return the following:

['the  quick brown', # 1 extra space on the left
'fox  jumps  over', # 2 extra spaces distributed evenly
'the   lazy   dog'] # 4 extra spaces distributed evenly
'''
import unittest
from itertools import cycle
from typing import List


def length(wl: List[str]) -> int:
    return sum(map(lambda x: len(x), wl))


def space(wl: List[str], k: int) -> str:
    if len(wl) is 1:
        return wl[0] + (k - len(wl[0])) * ' '
    needed_spaces = k - length(wl)
    i = cycle(range(len(wl) - 1))
    for _ in range(needed_spaces):
        wl[next(i)] += ' '
    return ''.join(wl)


def justify(wl: List[str], k: int) -> List[str]:
    justified = []  # type: List[str]
    line = [wl.pop(0)]
    while wl:
        if length(line) + len(line) + len(wl[0]) <= k:
            line.append(wl.pop(0))
        else:
            justified.append(space(line, k))
            line = []
    justified.append(space(line, k))
    return justified


class TestSolution(unittest.TestCase):
    def test_justify_given(self) -> None:
        wl = ['the', 'quick', 'brown', 'fox', 'jumps',
              'over', 'the', 'lazy', 'dog']
        justified = [
            'the  quick brown',  # 1 extra space on the left
            'fox  jumps  over',  # 2 extra spaces distributed evenly
            'the   lazy   dog']  # 4 extra spaces distributed evenly
        self.assertEqual(justify(wl, 16), justified)

    def test_justify_one_word(self) -> None:
        wl = ['the']
        justified = ['the             ']
        self.assertEqual(justify(wl, 16), justified)

    def test_space_one_word(self) -> None:
        wl = ['brown']
        justified = 'brown     '
        self.assertEqual(space(wl, 10), justified)

    def test_space_two_words(self) -> None:
        wl = ['brown', 'fox']
        justified = 'brown  fox'
        self.assertEqual(space(wl, 10), justified)

    def test_space_three_words(self) -> None:
        wl = ['the', 'brown', 'fox']
        justified = 'the  brown fox'
        self.assertEqual(space(wl, 14), justified)

    def test_length(self) -> None:
        self.assertEqual(length(['the', 'quick', 'brown']), 13)


if __name__ == '__main__':
    unittest.main()
