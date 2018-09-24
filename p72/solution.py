"""
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring
letter along that path.
For example, if a path in the graph goes through "ABACA",
the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges,
return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the
i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices
[0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
"""
import unittest
from typing import Optional, List, Tuple, Generator
from collections import Counter


def generate_paths(graph: str,
                   edges: List[Tuple[int, int]],
                   path: List[int]=[]
                   ) -> Generator[Optional[List[int]], None, None]:
    if not path:
        for e in edges:
            yield from generate_paths(graph, edges, list(e))
    else:
        options = [dest for orig, dest in edges if orig == path[-1]]
        if not options:
            yield path
        else:
            for d in options:
                if d in path:
                    yield None
                yield from generate_paths(graph, edges, path + [d])


def path_value(graph: str, path: Optional[List[int]]) -> Optional[int]:
    if path is None:
        return None
    return Counter(map(lambda x: graph[x], path)).most_common(1)[0][1]


def max_path_value(graph: str, edges: List[Tuple[int, int]]) -> Optional[int]:
    mv = 1
    for p in generate_paths(graph, edges):
        v = path_value(graph, p)
        if v is None:
            return None
        if v > mv:
            mv = v
    return mv


class TestSolution(unittest.TestCase):
    def test_ABACA(self) -> None:
        g = 'ABACA'
        e = [
            (0, 1),
            (0, 2),
            (2, 3),
            (3, 4)
        ]
        self.assertEqual(max_path_value(g, e), 3)

    def test_A(self) -> None:
        g = 'A'
        e = [(0, 0)]
        self.assertEqual(max_path_value(g, e), None)


if __name__ == '__main__':
    unittest.main()
