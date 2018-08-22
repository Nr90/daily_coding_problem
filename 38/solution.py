"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N,
returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""
import unittest
from typing import List


def create_board(size: int) -> List[List[int]]:
    return [[0] * size for _ in range(size)]


def is_valid(board: List[List[int]], row: int, col: int, size: int) -> bool:
    # check for queens on this row
    if any(board[row]):
        return False

    # check for queens to the top left on the diagonal
    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy]:
            return False
        ix -= 1
        iy -= 1

    # check for queens to the top right on the diagonal
    ix, iy = row, col
    while ix < size and iy >= 0:
        if board[ix][iy]:
            return False
        ix += 1
        iy -= 1
    return True


def solve_n(board: List[List[int]], col: int, size: int) -> int:
    n_solutions = 0
    for i in range(size):
        if is_valid(board, i, col, size):
            if col == size - 1:
                return 1
            board[i][col] = 1
            n_solutions += solve_n(board, col+1, size)
            # backtrack the last added queen
            board[i][col] = 0
    return n_solutions


def num_solutions(size: int) -> int:
    return solve_n(create_board(size), 0, size)


class TestSolution(unittest.TestCase):
    def test_create_board(self) -> None:
        self.assertEqual(
            create_board(3),
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ])

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
