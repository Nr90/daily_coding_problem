"""
This problem was asked by Twitter.

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that s as a prefix.

For example,
given the query string de and the set of strings [door, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary
into a more efficient data structure to speed up queries.
"""
import unittest
from typing import Iterator, List


def simple_autocomplete(s: str, possible: List[str]) -> Iterator[str]:
    return filter(lambda x: x.startswith(s), possible)


class TestSolutions(unittest.TestCase):
    def test_empty_query(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(simple_autocomplete('', ['door', 'deer', 'deal'])),
            sorted(['door', 'deer', 'deal'])
        )

    def test_non_matching_query(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(simple_autocomplete('elbert', ['door', 'deer', 'deal'])),
            sorted([])
        )

    def test_given_example(self: 'TestSolutions') -> None:
        self.assertEqual(
            sorted(simple_autocomplete('de', ['door', 'deer', 'deal'])),
            sorted(['deer', 'deal'])
        )


if __name__ == '__main__':
    unittest.main()
