"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit
you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10],
you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
import unittest
from typing import List


def max_profit(stock_hist: List[int]) -> int:
    profit = 0
    timesteps = len(stock_hist)
    for idx, price in enumerate(stock_hist):
        if idx >= timesteps - 2:
            break
        potential = max(stock_hist[idx+1:]) - price
        if potential > profit:
            profit = potential
    return profit


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(max_profit([9, 11, 8, 5, 7, 10]), 5)


if __name__ == '__main__':
    unittest.main()
