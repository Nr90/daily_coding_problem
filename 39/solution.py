"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite
two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally,
vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live
cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates,
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*)
and a dead cell with a dot (.).
"""
import unittest
from operator import itemgetter
from random import choice
from typing import List, Tuple


def create_board(living: List[Tuple[int, int]]) -> List[List[str]]:
    min_r = min(living, key=itemgetter(0))[0]
    max_r = max(living, key=itemgetter(0))[0]
    rows = max_r - min_r + 1
    min_c = min(living, key=itemgetter(1))[1]
    max_c = max(living, key=itemgetter(1))[1]
    cols = max_c - min_c + 1
    board = [['.'] * cols for _ in range(rows)]
    for cell in living:
        x = cell[0] - min_r
        y = cell[1] - min_c
        board[x][y] = '*'
    return board


def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(''.join(row))


def count_neighbours(board: List[List[str]], x: int, y: int) -> int:
    height = len(board)
    width = len(board[0])
    living_neighbours = 0

    # check for living left of cell
    if y > 0 and board[x][y-1] == '*':
        living_neighbours += 1

    # check for living top-left of cell
    if x > 0 and y > 0 and board[x-1][y-1] == '*':
        living_neighbours += 1

    # check for living top-right of cell
    if x > 0 and y < width - 1 and board[x-1][y+1] == '*':
        living_neighbours += 1

    # check for living bottom-left of cell
    if x < height - 1 and y > 0 and board[x+1][y-1] == '*':
        living_neighbours += 1

    # check for living bottom-right of cell
    if x < height - 1 and y < width - 1 and board[x+1][y+1] == '*':
        living_neighbours += 1

    # check for living above cell
    if x > 0 and board[x-1][y] == '*':
        living_neighbours += 1

    # check for living below cell
    if x < height - 1 and board[x+1][y] == '*':
        living_neighbours += 1

    # check for living right of cell
    if y < width - 1 and board[x][y+1] == '*':
        living_neighbours += 1
    return living_neighbours


def update_board(board: List[List[str]]) -> None:
    for ix, row in enumerate(board):
        for ij in range(len(row)):
            neighbours = count_neighbours(board, ix, ij)
            if neighbours == 3:
                board[ix][ij] = '*'
            elif neighbours == 2 and board[ix][ij] == '*':
                continue
            else:
                board[ix][ij] = '.'


def game_of_life(living: List[Tuple[int, int]], steps: int) -> None:
    board = create_board(living)
    print('Initial boardstate:')
    print_board(board)
    print('\n')
    for i in range(1, steps + 1):
        update_board(board)
        print(f'Iteration {i} boardstate:')
        print_board(board)
        print('\n')


class TestSolution(unittest.TestCase):
    def test_count_neighbours_none(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.']
        ], 0, 1), 0)
        self.assertEqual(count_neighbours([
            ['.'],
            ['.'],
            ['.']
        ], 1, 0), 0)

    def test_count_neighbours_top(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '*', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ], 1, 1), 1)

    def test_count_neighbours_top_right(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '*'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ], 1, 1), 1)

    def test_count_neighbours_top_left(self) -> None:
        self.assertEqual(count_neighbours([
            ['*', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ], 1, 1), 1)

    def test_count_neighbours_left(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.'],
            ['*', '.', '.'],
            ['.', '.', '.']
        ], 1, 1), 1)

    def test_count_neighbours_right(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.'],
            ['.', '.', '*'],
            ['.', '.', '.']
        ], 1, 1), 1)

    def test_count_neighbours_bottom(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '*', '.']
        ], 1, 1), 1)

    def test_count_neighbours_bottom_right(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '*']
        ], 1, 1), 1)

    def test_count_neighbours_bottom_left(self) -> None:
        self.assertEqual(count_neighbours([
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['*', '.', '.']
        ], 1, 1), 1)

    def test_create_board(self) -> None:
        self.assertEqual(create_board([(1, 0), (3, 1)]), [
            ['*', '.'],
            ['.', '.'],
            ['.', '*']
        ])

    def test_game_of_life(self) -> None:
        # output is not checked, only if runs without failure
        members = 300
        x_options = range(25)
        y_options = range(50)
        iters = 10
        game_of_life([
            (choice(x_options) + 3, choice(y_options) + 20)
            for _ in range(members)
        ], iters)


if __name__ == '__main__':
    unittest.main()
