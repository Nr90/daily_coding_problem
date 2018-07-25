"""
This problem was asked by Twitter.

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that s as a prefix.

For example, given the query string de and the set of strings [door, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
import unittest
from typing import List
 


def simple_autocomplete(s: str, possible: List[str]) -> List[str]:
    return filter(lambda x: x.startswith(s), possible)


class TestSolutions(unittest.TestCase):
    def test_simple_autocomplete(self: 'TestSolutions') -> None:
        test_cases = [
            ('de', ['door', 'deer', 'deal'], ['deer', 'deal']),
            ('', ['door', 'deer', 'deal'], ['door', 'deer', 'deal']),
            ('elbert', ['door', 'deer', 'deal'], [])
        ]
        for c in test_cases:
            self.assertEqual(
                sorted(simple_autocomplete(c[0], c[1])),
                sorted(c[2]))



if __name__ == '__main__':
    unittest.main()
