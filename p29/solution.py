"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters
as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists
solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""
import unittest


def encode(s: str) -> str:
    if not s:
        return ''
    counter = 1
    char = s[1]
    encoded = ''
    for c in s[1:]:
        if c is char:
            counter += 1
        else:
            encoded += f'{counter}{char}'
            char = c
            counter = 1
    encoded += f'{counter}{char}'
    return encoded


def decode(s: str) -> str:
    if not s:
        return ''
    counter = int(s[0])
    decoded = counter * s[1]
    for i, c in enumerate(s[2:]):
        if i % 2 is 0:
            counter = int(c)
        else:
            decoded += counter * c
    return decoded


class TestSolution(unittest.TestCase):
    def test_given_encode(self) -> None:
        self.assertEqual(encode('AAAABBBCCDAA'), '4A3B2C1D2A')

    def test_given_decode(self) -> None:
        self.assertEqual(decode('4A3B2C1D2A'), 'AAAABBBCCDAA')


if __name__ == '__main__':
    unittest.main()
