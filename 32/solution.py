"""
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates,
represented as a 2D array.
Determine whether there is a possible arbitrage:
that is, whether there is some sequence of trades you can make,
starting with some amount A of any currency,
so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
