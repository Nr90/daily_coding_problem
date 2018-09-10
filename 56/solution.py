"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
"""
import unittest
from typing import List


def valid(graph: List[List[int]], colors: List[int]):
    last_vertex, last_color = len(colors) - 1, colors[-1]
    colored_neighbors = [
        i for i, has_edge in enumerate(graph[last_vertex])
        if has_edge and i < last_vertex
    ]
    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False
    return True


# https://www.dailycodingproblem.com/blog/graph-coloring/
def colorable(graph: List[List[int]], k: int, colors: List[int]=[]):
    if len(colors) == len(graph):
        return True
    for i in range(k):
        colors.append(i)
        if valid(graph, colors):
            if colorable(graph, k, colors):
                return True
        colors.pop()
    return False


class TestSolution(unittest.TestCase):
    m = [
        [0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ]

    def test_k1(self) -> None:
        self.assertFalse(colorable(self.m, 1))

    def test_k2(self) -> None:
        self.assertFalse(colorable(self.m, 2))

    def test_k3(self) -> None:
        self.assertTrue(colorable(self.m, 3))

    def test_k4(self) -> None:
        self.assertTrue(colorable(self.m, 4))

    def test_k5(self) -> None:
        self.assertTrue(colorable(self.m, 5))

    def test_k6(self) -> None:
        self.assertTrue(colorable(self.m, 6))

if __name__ == '__main__':
    unittest.main()
