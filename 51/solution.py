"""
This problem was asked by Facebook.

Given a function that generates perfectly random numbers
between 1 and k (inclusive), where k is an input,
write a function that shuffles a deck of cards represented
as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import unittest
from random import randint
from typing import List, Dict
from collections import defaultdict


def shuffle(deck: List[str]) -> List[str]:
    n = len(deck)
    for i in range(n):
        rand_j = randint(i, n-1)
        deck[i], deck[rand_j] = deck[rand_j], deck[i]
    return deck


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        deck = ['Ahearts', 'Kclubs', 'Jdiamonds', '10spades']
        perms = defaultdict(lambda: 0)  # type: Dict[str, int]
        for _ in range(1000000):
            perms[','.join(shuffle(deck))] += 1
        self.assertTrue(max(perms.values()) - min(perms.values()) < 1000)


if __name__ == '__main__':
    unittest.main()
