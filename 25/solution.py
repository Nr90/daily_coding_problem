"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.

For example, given the regular expression "ra." and the string "ray",
your function should return true.
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat",
your function should return true.
The same regular expression on the string "chats" should return false.
"""
import unittest


def match(c1: str, c2: str) -> bool:
    if c1 is '.' or c2 is '.':
        return True
    if c1 is c2:
        return True
    return False


def regex(re: str, s: str) -> bool:
    rel = list(re)
    sl = list(s)
    prev = ''
    while rel:
        c = rel.pop(0)
        if c is '*':
            while len(sl) > 1 and match(sl[0], prev) and sl[1] is not rel[1]:
                sl.pop(0)
        elif c is '.':
            sl.pop(0)
        else:
            if c is not sl[0]:
                return False
            sl.pop(0)
        prev = c
    if sl:
        return False
    return True


class TestSolution(unittest.TestCase):
    def test_ray(self) -> None:
        self.assertTrue(regex('ra.', 'ray'))

    def test_raymond(self) -> None:
        self.assertFalse(regex('ra.', 'raymond'))

    def test_chat(self) -> None:
        self.assertTrue(regex('.*at', 'chat'))

    def test_chats(self) -> None:
        self.assertFalse(regex('.*at', 'chats'))


if __name__ == '__main__':
    unittest.main()
