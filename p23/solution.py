"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall.
Each False, boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach
the end coordinate from the start.
If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.

For example, given the following board:

[[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2)
because there is a wall everywhere else on the second row.
"""
import unittest
from typing import List, Tuple, Optional


def find_moves(board: List[List[bool]],
               pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    moves = []  # type: List[Tuple[int, int]]
    if pos[0] > 0 and not board[pos[0] - 1][pos[1]]:
        moves += [(pos[0] - 1, pos[1])]
    if pos[0] < len(board) - 1 and not board[pos[0] + 1][pos[1]]:
        moves += [(pos[0] + 1, pos[1])]
    if pos[1] > 0 and not board[pos[0]][pos[1] - 1]:
        moves += [(pos[0], pos[1] - 1)]
    if pos[1] < len(board[0]) - 1 and not board[pos[0]][pos[1] + 1]:
        moves += [(pos[0], pos[1] + 1)]
    return moves


def search(board: List[List[bool]],
           start: Tuple[int, int],
           end: Tuple[int, int]) -> Optional[int]:
    if start == end:
        return 0
    p_moves = find_moves(board, start)
    if not p_moves:
        return None
    board[start[0]][start[1]] = True
    for m in p_moves:
        board[m[0]][m[1]] = True
    steps = None
    for m in p_moves:
        s = search(board, m, end)
        if s is not None:
            steps = min(steps, s + 1) if steps else s + 1
    return steps


class TestSolution(unittest.TestCase):
    def test_find_moves(self) -> None:
        board = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        pos = (3, 0)
        moves = [(2, 0), (3, 1)]
        self.assertEqual(find_moves(board, pos), moves)
        pos = (3, 3)
        moves = [(2, 3), (3, 2)]
        self.assertEqual(find_moves(board, pos), moves)
        pos = (0, 0)
        moves = [(0, 1)]
        self.assertEqual(find_moves(board, pos), moves)
        pos = (1, 2)
        moves = [(0, 2), (2, 2)]
        self.assertEqual(find_moves(board, pos), moves)
        pos = (2, 1)
        moves = [(3, 1), (2, 0), (2, 2)]
        self.assertEqual(find_moves(board, pos), moves)

    def test_given(self) -> None:
        board = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        start = (3, 0)
        end = (0, 0)
        self.assertEqual(search(board, start, end), 7)

    def test_start_equals_end(self) -> None:
        board = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        start = (3, 0)
        end = (3, 0)
        self.assertEqual(search(board, start, end), 0)

    def test_no_solution(self) -> None:
        board = [
            [False, True, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]
        start = (0, 0)
        end = (3, 0)
        self.assertEqual(search(board, start, end), None)


if __name__ == '__main__':
    unittest.main()
