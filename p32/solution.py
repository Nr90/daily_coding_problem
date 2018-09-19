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
from math import log
from typing import List


# fixed code from:
# https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python/
def arbitrage(table: List[List[float]]) -> bool:
    transformed_graph = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for _ in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


class TestSolution(unittest.TestCase):
    def test_one_currency(self) -> None:
        table = [
            [2.0],
        ]
        self.assertTrue(arbitrage(table))
        table = [
            [1.0],
        ]
        self.assertFalse(arbitrage(table))

    def test_two_currencies(self) -> None:
        table = [
            [1.0, 1.1],
            [1.1, 1.0],
        ]
        self.assertTrue(arbitrage(table))
        table = [
            [1.0, 1.2],
            [0.8, 1.0],
        ]
        self.assertFalse(arbitrage(table))


if __name__ == '__main__':
    unittest.main()
