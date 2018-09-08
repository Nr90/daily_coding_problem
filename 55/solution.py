"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

    shorten(url),
        which shortens the url into a six-character alphanumeric string,
        such as zLg6wl.

    restore(short),
        which expands the shortened string into the original url.
        If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""
import unittest
from collections import defaultdict
from base64 import b64encode
from hashlib import md5
from typing import Dict


class URLShortener:
    def __init__(self) -> None:
        self.urls = defaultdict(lambda: None)  # type: Dict[str, str]

    # https://www.peterbe.com/plog/best-hashing-function-in-python
    def h6(self, s: str) -> str:
        return str(b64encode(md5(s.encode('utf-8')).digest())[:6])

    def shorten(self, url: str) -> str:
        short = self.h6(url)
        self.urls[short] = url
        return short

    def restore(self, short: str) -> str:
        return self.urls[short]


class TestSolution(unittest.TestCase):
    def test_shorten_restore(self) -> None:
        url = 'http://www.google.com/'
        shortener = URLShortener()
        short = shortener.shorten(url)
        self.assertEqual(url, shortener.restore(short))

    def test_same_url_same_short(self) -> None:
        url = 'http://www.google.com/'
        shortener = URLShortener()
        self.assertEqual(
            shortener.shorten(url),
            shortener.shorten(url)
        )

    def test_missing_short(self) -> None:
        shortener = URLShortener()
        short = 'zLg6wl'
        self.assertEqual(None, shortener.restore(short))


if __name__ == '__main__':
    unittest.main()
