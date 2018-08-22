"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N,
returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""
import unittest


def num_solutions(size: int) -> int:
    return 1


class TestSolution(unittest.TestCase):
    def test_n_queens(self) -> None:
        testtable = [
            (1, 1),
            (2, 0),
            (3, 0),
            (4, 2),
            (5, 10),
            (6, 4),
            (7, 40),
            (8, 92)
        ]
        for t in testtable:
            with self.subTest(i=t[0]):
                self.assertEqual(num_solutions(t[0]), t[1])


if __name__ == '__main__':
    unittest.main()
