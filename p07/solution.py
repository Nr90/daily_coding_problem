"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""
import unittest


def count_ways(message: str) -> int:
    if len(message) <= 1:
        return 1
    if int(message[0:2]) > 26:
        return count_ways(message[1:])
    if message[1] == '0':
        return count_ways(message[2:])
    return count_ways(message[1:]) + count_ways(message[2:])


class TestSolutions(unittest.TestCase):
    def test_count_ways(self: 'TestSolutions'):
        self.assertEqual(count_ways(''), 1)
        self.assertEqual(count_ways('1'), 1)
        self.assertEqual(count_ways('10'), 1)
        self.assertEqual(count_ways('101'), 1)
        self.assertEqual(count_ways('1010'), 1)
        self.assertEqual(count_ways('27'), 1)
        self.assertEqual(count_ways('111'), 3)


if __name__ == '__main__':
    unittest.main()
